"""Kindred Care tier economics - read from the model's own cells, not inferred.
Source: 'Kindred Care - Pricing Model_v1_DRAFT_Brad_May1_26' sheets 1, 2, 4.
Run: python3 kindred-care/finance/unit_cost_model.py
"""
FX = 1.55
SUPPORT_YR = 500 * 12 * FX     # AUD 9,300 - Assumptions 1.2, FIXED PER TENANT.
                               # Cost Engine row 21 sets it to 0: excluded from tier GM
                               # by design, pending cover review item (2).
GCP_YR = 0.75 * 12 * FX        # AUD 13.95 per active mother per year, post-credit

# Sheet 4 'B2B Health Pricing' rows 7-10, verbatim.
# Sheet 2 'Cost Engine' row 26 supplies var cost/active mother/month at each scale point.
TIERS = [
    # name         births      licence  incl_enrolled  active  var_mo
    ("Foundation", "up to 500",  28000,   300,           120,   5.8745),
    ("Standard",   "501-1,500",  48000,   900,           360,   4.3369),
    ("Network",    "1,501-3,500",72000,  2000,           800,   3.9897),
    ("Enterprise", "3,500+",     95000,  5000,          2000,   3.7169),
]

print("=== The model's own tier economics (sheet 4, verified) ===")
print(f"{'Tier':<12}{'Births':<14}{'Licence':>9}{'Incl':>7}{'Active':>8}"
      f"{'Var cost':>11}{'GM':>8}{'GM +support':>13}")
for n, b, lic, incl, act, vm in TIERS:
    var = act * vm * 12
    gm  = (lic - var) / lic
    gm2 = (lic - var - SUPPORT_YR) / lic
    print(f"{n:<12}{b:<14}{lic:>9,}{incl:>7,}{act:>8,}{var:>11,.0f}"
          f"{gm:>7.1%}{gm2:>13.1%}")
print(f"\n  Sheet 4 publishes 70% / 61% / 47% / 6% -- reproduced exactly above.")
print(f"  '+support' adds AUD {SUPPORT_YR:,.0f}/yr, which the model deliberately excludes.\n")

print("=== Avatar share of variable cost, per active mother per year ===")
for n, _, _, _, _, vm in TIERS:
    yr = vm * 12
    av = yr - GCP_YR
    print(f"  {n:<12} total AUD {yr:6.2f}   avatar {av:6.2f} ({av/yr:4.0%})"
          f"   everything else {GCP_YR:5.2f}")
print("  Cost Engine row 13: HeyGen rate ALREADY falls with volume")
print("  ($0.19 -> $0.128 -> $0.114 -> $0.103 USD/min). Hector's bundle comment is modelled.\n")

print("=== Brad's question: can an entry tier sit under $20,000? ===")
print("  Reduce INCLUDED mothers, not price. Foundation unit cost AUD 5.8745/active/mo.")
for incl in (100, 150, 200, 250, 300):
    act = incl * 0.40
    var = act * 5.8745 * 12
    cost = var + SUPPORT_YR
    for price in (18000, 19500):
        gm = (price - cost) / price
        print(f"  {incl:>3} enrolled ({act:>3.0f} active): cost AUD {cost:7,.0f}"
              f"  at ${price:,} -> GM {gm:6.1%}"
              f"{'   <-- support is ' + format(SUPPORT_YR/cost, '.0%') + ' of cost' if price==18000 else ''}")
