#!/usr/bin/env python3
"""ICU/CCU bed and staffing check for the after-hours manager.

Deterministic arithmetic so the agent never guesses the numbers. No patient
identifiers go in: counts and bed labels only.

Example:
  python3 icu_check.py --shift night --beds 6 --occupied 5 --one-to-one 1 \
      --ward-status 2 --expected-admissions 1
"""
import argparse
import json
import math
from pathlib import Path

CONFIG = json.loads((Path(__file__).parent / "unit-config.json").read_text())["icu_ccu"]


def rn_required(one_to_one, one_to_two, ward_status):
    r = CONFIG["ratios"]
    need = one_to_one * r["one_to_one"] + one_to_two * r["one_to_two"] + ward_status * r["ward_status"]
    return max(CONFIG["min_rn_on_floor"], math.ceil(need))


def assess(a):
    beds = a.beds if a.beds is not None else CONFIG["funded_beds"]
    if beds is None:
        raise SystemExit("Total ICU/CCU beds unknown: pass --beds or set funded_beds in unit-config.json")
    if a.one_to_one + a.ward_status > a.occupied:
        raise SystemExit("1:1 plus ward-status patients cannot exceed occupied beds")

    one_to_two = a.occupied - a.one_to_one - a.ward_status
    rostered = a.rostered if a.rostered is not None else CONFIG["rostered_rn"][a.shift]
    free = beds - a.occupied
    target = CONFIG["reserved_admission_beds_target"]
    minimum = CONFIG["reserved_admission_beds_min"]
    need_now = rn_required(a.one_to_one, one_to_two, a.ward_status)
    # Assume an unplanned admission arrives 1:1 until proven otherwise.
    need_with_adm = rn_required(a.one_to_one + a.expected_admissions, one_to_two, a.ward_status)

    out = {"shift": a.shift, "beds": beds, "occupied": a.occupied, "free": free,
           "acuity": {"1:1": a.one_to_one, "1:2": one_to_two, "ward_status": a.ward_status},
           "rn_rostered": rostered, "rn_required_now": need_now,
           "rn_required_if_admissions_arrive": need_with_adm, "actions": [], "risks": []}

    # Beds
    if free >= target:
        out["bed_status"] = "GREEN"
    elif free >= minimum:
        out["bed_status"] = "AMBER"
        out["actions"].append(f"Only {free} bed(s) free (target {target}). Line up ward-status patient(s) to cycle out; confirm ward beds now.")
    else:
        out["bed_status"] = "RED"
        out["actions"].append(f"No admission bed. Step down a ward-status patient now ({a.ward_status} available) or escalate to exec on call.")
    if free < target and a.ward_status == 0:
        out["risks"].append("No ward-status patients to cycle out: buffer depends on transfer/discharge of an ICU-acuity patient.")
    if free < target and a.ward_status > 0:
        n = min(a.ward_status, target - free)
        out["actions"].append(f"Identify {n} ward-status patient(s) as first to move; ward bed and receiving RN confirmed before handover.")

    # Staffing
    thr = CONFIG["cancel_one_rn_at_or_below_patients"]
    if rostered > need_now and a.occupied <= thr:
        if need_with_adm > rostered - 1:
            out["staffing"] = "CANCEL ONE RN - CONDITIONAL"
            out["risks"].append(f"After cancelling, {rostered - 1} RN(s) cover current patients but not an unplanned 1:1 admission (needs {need_with_adm}). Only cancel if on-call/recall RN is confirmed or bed is held closed.")
        else:
            out["staffing"] = "CANCEL ONE RN - OK"
        out["actions"].append(f"Patient load {a.occupied} <= {thr}: one RN may be cancelled (floor minimum {CONFIG['min_rn_on_floor']}). Offer as redeploy to ward before cancelling outright.")
    elif rostered < need_now:
        out["staffing"] = "SHORT"
        out["actions"].append(f"Short {need_now - rostered} RN for current acuity. Call casual/agency/overtime; consider redeploy from ward with ICU-competent RN.")
    else:
        out["staffing"] = "HOLD"
        if a.occupied <= thr and rostered <= need_now:
            out["risks"].append(f"Patient load {a.occupied} <= {thr} but acuity needs all {rostered} RNs: do not cancel.")
    if need_with_adm > rostered:
        out["risks"].append(f"An unplanned 1:1 admission would need {need_with_adm} RNs vs {rostered} rostered: know who you'd call.")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--shift", choices=["day", "night"], required=True)
    p.add_argument("--beds", type=int, help="Total open ICU/CCU beds tonight")
    p.add_argument("--occupied", type=int, required=True)
    p.add_argument("--one-to-one", type=int, default=0, help="Patients needing 1:1 (ventilated, unstable, etc.)")
    p.add_argument("--ward-status", type=int, default=0, help="Patients fit for ward, waiting on a bed")
    p.add_argument("--expected-admissions", type=int, default=1)
    p.add_argument("--rostered", type=int, help="RNs actually on shift (defaults to roster)")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    r = assess(a)
    if a.json:
        print(json.dumps(r, indent=2))
        return
    print(f"ICU/CCU {r['shift']}: {r['occupied']}/{r['beds']} occupied, {r['free']} free -> beds {r['bed_status']}")
    print(f"Acuity 1:1={r['acuity']['1:1']} 1:2={r['acuity']['1:2']} ward-status={r['acuity']['ward_status']}")
    print(f"RN rostered {r['rn_rostered']}, required now {r['rn_required_now']}, with admission {r['rn_required_if_admissions_arrive']} -> {r['staffing']}")
    for x in r["actions"]:
        print(f"ACTION: {x}")
    for x in r["risks"]:
        print(f"RISK: {x}")


if __name__ == "__main__":
    main()
