"""Kindred Care unit cost - rebuilt from Hector's own cost engine.
Sources: 'BoR AI Avatar Pricing' (hector@clinops.cloud) and
'Kindred Care - Pricing Model_v1_DRAFT_Brad_May1_26' sheets 1-4.
Run: python3 kindred-care/finance/unit_cost_model.py
"""
FX          = 1.55      # AUD per USD (Assumptions 1.1, RBA Apr 2026)
HEYGEN_MIN  = 0.19      # USD/min  (USD475 plan / 5000 credits x 0.5 min)
HEYGEN_BUND = 0.128     # USD/min  Hector's larger-bundle rate, comment 26 May (OPEN)
GCP_MO      = 0.75      # USD per active mother per month, post-credit (Hector F67)
SUPPORT_MO  = 500       # USD per service per month, FIXED PER TENANT (Hector F10)
SETUP       = 12000     # USD one-off per customer
AVATAR_MIN  = 40        # min per active mother per month (Hector F86)
ENGAGEMENT  = 0.40      # active mothers as % of enrolled (Assumptions 1.3)

def var_per_active_yr(minutes=AVATAR_MIN, rate=HEYGEN_MIN, uptake=0.40, gcp=True):
    """AUD variable cost per ACTIVE mother per year."""
    usd_mo = minutes * uptake * rate + (GCP_MO if gcp else 0)
    return usd_mo * 12 * FX

print("=== Reconciling the model's own published figure ===")
v = var_per_active_yr()
print(f"  at 40% uptake: AUD {v/12:5.2f}/mo  -> AUD {v:6.2f}/yr")
print(f"  Sheet 3 'Margin Tiers' publishes AUD $5.87/mo. Match: {abs(v/12-5.87)<0.01}")
print(f"  NOTE: reconciles at 40% (the ENGAGEMENT rate), not the 35% video uptake")
print(f"        stated in Assumptions 1.2. Likely a mis-referenced cell.")
print(f"  -> AUD {v:.2f}/yr is the '$70.44' figure. Not a contradiction: it is")
print(f"     variable cost per ACTIVE mother per year.\n")

print("=== Cost driver split, per active mother per year ===")
av  = AVATAR_MIN * 0.40 * HEYGEN_MIN * 12 * FX
gcp = GCP_MO * 12 * FX
print(f"  Avatar video : AUD {av:6.2f}  ({av/(av+gcp)*100:.0f}%)")
print(f"  GCP everything else: AUD {gcp:6.2f}  ({gcp/(av+gcp)*100:.0f}%)\n")

def service(births, licence, minutes=AVATAR_MIN, rate=HEYGEN_MIN, label=""):
    enrolled = births            # model uses a 12-month enrolled period
    active   = enrolled * ENGAGEMENT
    variable = active * var_per_active_yr(minutes, rate)
    support  = SUPPORT_MO * 12 * FX
    total    = variable + support
    gm       = (licence - total) / licence * 100
    print(f"  {label:38s} cost AUD {total:9,.0f}  licence {licence:7,}  "
          f"margin {gm:7.1f}%  {'LOSS' if gm<0 else ''}")
    return total

print("=== A 1,000-birth service (400 active mothers) ===")
print("   [+ one-off setup AUD {:,.0f} on top of every line below]".format(SETUP*FX))
service(1000, 25000, label="as modelled, $25k tier")
service(1000, 18000, label="as modelled, at a sub-$20k tier")
service(1000, 25000, rate=HEYGEN_BUND, label="Hector's bundle rate $0.128/min")
service(1000, 25000, minutes=20, label="avatar capped at 20 min/mother/mo")
service(1000, 25000, minutes=10, label="avatar capped at 10 min/mother/mo")
service(1000, 25000, minutes=0,  label="voice + text only, no avatar video")
print()

print("=== The top of the schedule (the cover note's own warning) ===")
service(12500, 95000, label="5,000 active @ $95k Enterprise")
service(12500, 135000, label="...at the cover's proposed $135k fix")
print()

print("=== Break-even licence at 10 avatar min/mo, by service size ===")
for b in (300, 500, 1000, 2000, 3500):
    active = b * ENGAGEMENT
    cost = active * var_per_active_yr(minutes=10) + SUPPORT_MO*12*FX
    print(f"  {b:5,} births ({active:5,.0f} active): break-even AUD {cost:8,.0f}"
          f"   at 40% GM needs AUD {cost/0.6:8,.0f}")
