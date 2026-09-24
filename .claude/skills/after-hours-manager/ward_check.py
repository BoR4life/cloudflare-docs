#!/usr/bin/env python3
"""Ward bed and staffing check for the after-hours manager.

Uses the unit's patients_per_nurse ratio from unit-config.json. Counts only,
no patient identifiers.

Example:
  python3 ward_check.py --unit g_pavilion --shift night --occupied 30 --rostered 3 \
      --expected-admissions 2
"""
import argparse
import json
import math
from pathlib import Path

UNITS = json.loads((Path(__file__).parent / "unit-config.json").read_text())["units"]


def nurses_required(unit, shift, patients):
    per = unit.get("patients_per_nurse", {}).get(shift)
    if per is None:
        raise SystemExit(f"{unit['name']}: no {shift} ratio in unit-config.json")
    return max(unit.get("min_staff_on_floor") or 1, math.ceil(patients / per))


def assess(a):
    if a.unit not in UNITS:
        raise SystemExit(f"Unknown unit '{a.unit}'. Known: {', '.join(UNITS)}")
    u = UNITS[a.unit]
    beds = u.get("funded_beds")
    if beds is None:
        raise SystemExit(f"{u['name']}: bed count not set in unit-config.json")
    expected = a.occupied + a.expected_admissions - a.expected_discharges
    need_now = nurses_required(u, a.shift, a.occupied)
    need_exp = nurses_required(u, a.shift, expected)
    out = {"unit": u["name"], "shift": a.shift, "beds": beds, "occupied": a.occupied,
           "free": beds - a.occupied, "expected_by_end": expected,
           "ratio": f"1:{u['patients_per_nurse'][a.shift]}", "rostered": a.rostered,
           "required_now": need_now, "required_expected": need_exp, "actions": [], "risks": []}

    if expected > beds:
        out["actions"].append(f"Expected {expected} patients exceeds {beds} beds: divert {expected - beds} admission(s) to another ward or escalate.")
    usual = u.get("usual_occupancy")
    if usual and expected > usual[1]:
        out["risks"].append(f"Expected {expected} is above usual {usual[0]}-{usual[1]}: check skill mix and single-room availability.")

    if a.rostered is None:
        out["staffing"] = "UNKNOWN (pass --rostered)"
    elif a.rostered < need_exp:
        out["staffing"] = "SHORT"
        out["actions"].append(f"Short {need_exp - a.rostered} nurse(s) for {expected} patients at {out['ratio']}. Redeploy (ICU/CCU cancelled RN first), then casual, overtime, agency.")
    elif a.rostered > need_exp:
        out["staffing"] = "OVER"
        out["actions"].append(f"{a.rostered - need_exp} nurse(s) above ratio for {expected} patients: redeploy before cancelling.")
    else:
        out["staffing"] = "OK"
    if need_exp > need_now:
        out["risks"].append(f"Admissions tip staffing from {need_now} to {need_exp} nurses: sort cover before they arrive.")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--unit", required=True)
    p.add_argument("--shift", choices=["day", "evening", "night"], required=True)
    p.add_argument("--occupied", type=int, required=True)
    p.add_argument("--rostered", type=int, help="Nurses on the floor this shift")
    p.add_argument("--expected-admissions", type=int, default=0)
    p.add_argument("--expected-discharges", type=int, default=0)
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    r = assess(a)
    if a.json:
        print(json.dumps(r, indent=2))
        return
    print(f"{r['unit']} {r['shift']}: {r['occupied']}/{r['beds']} occupied, {r['free']} free, {r['expected_by_end']} expected by end of shift")
    print(f"Ratio {r['ratio']}: rostered {r['rostered']}, required now {r['required_now']}, expected {r['required_expected']} -> {r['staffing']}")
    for x in r["actions"]:
        print(f"ACTION: {x}")
    for x in r["risks"]:
        print(f"RISK: {x}")


if __name__ == "__main__":
    main()
