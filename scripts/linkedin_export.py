#!/usr/bin/env python3
"""Analyse a LinkedIn data-export zip against the CRM.

Usage:
  python3 scripts/linkedin_export.py linkedin-2026-09-10.zip [--prev linkedin-2026-06-01.zip]
                                     [--accounts sales/accounts.md] [--targets sales/linkedin-targets.md]

Outputs (stdout, markdown): network map against CRM accounts, champion movement since
the previous export, inbound invitations by organisation, DM threads mentioning CRM
accounts, publishing cadence, and coverage of the named target list.
No data is written anywhere; the zip stays where it is.
"""
import argparse, csv, io, re, sys, zipfile
from collections import Counter, defaultdict
from datetime import datetime

def read_csv(z, name):
    for n in z.namelist():
        if n.lower().endswith(name.lower()):
            raw = z.read(n).decode("utf-8-sig", errors="replace")
            # Connections.csv has a 3-line preamble
            lines = raw.splitlines()
            start = next((i for i, l in enumerate(lines) if l.startswith("First Name") or l.startswith("Date") or l.startswith("From") or l.startswith("CONVERSATION")), 0)
            return list(csv.DictReader(io.StringIO("\n".join(lines[start:]))))
    return []

STOP = {"the","of","and","hospital","health","service","services","university","college","pty","ltd","private","limited","group"}

def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).strip()

def squash(s):
    return norm(s).replace(" ", "")

def org_keys(account):
    """Short, distinctive keys for an account name: 'Southwest Hospital and Health Service'
    -> ['southwest']; 'Sunshine Coast Hospital and Health Service' -> ['sunshinecoast', 'sunshine coast'];
    'James Cook University' -> ['jamescook']. Also accepts 'south west' for 'southwest'."""
    name = account.split("—")[0]
    toks = [t for t in norm(name).split() if t not in STOP]
    keys = set()
    if toks:
        keys.add("".join(toks[:2]))
        keys.add(toks[0]) if len(toks[0]) >= 6 else None
    keys.add(squash(name))
    return {k for k in keys if k}

def text_has_org(text, account):
    sq = squash(text)
    return any(k in sq for k in org_keys(account))

def load_accounts(path):
    names = []
    try:
        for line in open(path, encoding="utf-8"):
            if line.startswith("## "):
                names.append(line[3:].strip())
    except FileNotFoundError:
        pass
    return names

def load_targets(path):
    try:
        return [l.strip("- ").strip() for l in open(path, encoding="utf-8") if l.startswith("- ")]
    except FileNotFoundError:
        return []

def org_match(company, accounts):
    if not company: return None
    for a in accounts:
        if text_has_org(company, a): return a
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("zip"); ap.add_argument("--prev"); ap.add_argument("--accounts", default="sales/accounts.md")
    ap.add_argument("--targets", default="sales/linkedin-targets.md")
    a = ap.parse_args()
    z = zipfile.ZipFile(a.zip)
    accounts = load_accounts(a.accounts); targets = [norm(t) for t in load_targets(a.targets)]
    conns = read_csv(z, "Connections.csv"); shares = read_csv(z, "Shares.csv")
    comments = read_csv(z, "Comments.csv"); invites = read_csv(z, "Invitations.csv")
    msgs = read_csv(z, "messages.csv")

    print(f"# LinkedIn export analysis — {a.zip}\n")
    print(f"Connections {len(conns)} · Posts {len(shares)} · Comments made {len(comments)} · Invitations {len(invites)} · Messages {len(msgs)}\n")

    # 1. Network vs CRM accounts
    by_org = defaultdict(list)
    for c in conns:
        m = org_match(c.get("Company", ""), accounts)
        if m: by_org[m].append(c)
    print("## Connections inside CRM accounts")
    for org, ppl in sorted(by_org.items(), key=lambda kv: -len(kv[1])):
        print(f"- **{org}** ({len(ppl)}): " + "; ".join(f"{p.get('First Name','')} {p.get('Last Name','')} — {p.get('Position','')}" for p in ppl[:8]))
    print()

    # 2. Champion movement
    if a.prev:
        pz = zipfile.ZipFile(a.prev); prev = {(norm(p.get("First Name")), norm(p.get("Last Name"))): p for p in read_csv(pz, "Connections.csv")}
        moved = []
        for c in conns:
            k = (norm(c.get("First Name")), norm(c.get("Last Name")))
            if k in prev and norm(prev[k].get("Company")) != norm(c.get("Company")) and c.get("Company"):
                moved.append((c, prev[k]))
        print(f"## Champions who moved since {a.prev} ({len(moved)})")
        for c, p in moved:
            print(f"- {c['First Name']} {c['Last Name']}: {p.get('Company')} → **{c.get('Company')}** ({c.get('Position')})")
        print()

    # 3. Inbound invitations by org (received only)
    inbound = [i for i in invites if (i.get("Direction") or "").upper() == "INCOMING"]
    by_name = {norm(f"{c.get('First Name','')} {c.get('Last Name','')}"): c for c in conns}
    print(f"## Inbound connection requests ({len(inbound)})")
    rows = []
    for i in inbound:
        who = i.get("From", ""); c = by_name.get(norm(who), {})
        company = c.get("Company", ""); org = org_match(company, accounts)
        tag = "TARGET" if norm(who) in targets else ""
        rows.append((org or "—", who, company or "(company unknown — not yet a connection)", tag, i.get("Sent At","")))
    for org, who, company, tag, when in sorted(rows, key=lambda r: (r[0]=="—", r[0])):
        print(f"- {who} — {company}" + (f" → **{org}**" if org != "—" else "") + (f" [{tag}]" if tag else "") + f" ({when})")
    print()

    # 4. DMs mentioning CRM accounts
    print("## Message threads mentioning CRM accounts")
    hits = defaultdict(set)
    for m in msgs:
        text = " ".join(str(v) for v in m.values())
        for acc in accounts:
            if text_has_org(text, acc):
                hits[acc].add(m.get("CONVERSATION ID") or m.get("CONVERSATION TITLE") or m.get("FROM"))
    for acc, ids in sorted(hits.items(), key=lambda kv: -len(kv[1])): print(f"- {acc}: {len(ids)} thread(s)")
    print()

    # 5. Publishing cadence (last 12 weeks)
    print("## Posts per week, last 12 weeks")
    wk = Counter()
    for s in shares:
        d = s.get("Date") or ""
        try: wk[datetime.fromisoformat(d[:10]).strftime("%G-W%V")] += 1
        except ValueError: pass
    for w in sorted(wk)[-12:]: print(f"- {w}: {wk[w]}")
    print()

    # 6. Target-list coverage from Brad's own comments
    if targets:
        touched = Counter()
        for cm in comments:
            text = norm(" ".join(str(v) for v in cm.values()))
            for t in targets:
                if t and t in text: touched[t] += 1
        print(f"## Target list: {len(touched)}/{len(targets)} people commented on")
        for t, n in touched.most_common(): print(f"- {t}: {n}")

if __name__ == "__main__":
    main()
