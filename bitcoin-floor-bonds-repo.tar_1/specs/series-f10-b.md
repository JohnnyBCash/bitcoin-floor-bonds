# Floor Bond Series F10-B (Junior, 10-Year Fixed Coupon)

## Product Summary

| Parameter | Value |
|-----------|-------|
| Product | Series F10-B |
| Tranche | Junior (30% of issuance) |
| Term | 10 years |
| Face value | $10,000 per unit |
| Coupon type | Fixed annual |
| K-factor | 0.35 |
| Coupon rate | 12.60% |
| Annual payment | $1,260 per $10,000 face |
| Target buyer | Family offices, credit funds seeking long-duration high yield |

## Risk Profile

High yield equivalent. First-loss position with 10-year exposure. Compensated by highest fixed coupon in the shelf.

## Reference Issuance (January 1, 2027)

| Parameter | Value |
|-----------|-------|
| BFR at issuance | 35.99% (exact compound) |
| Trend price | $166,749 |
| Floor (0.432x) | $72,036 |
| Floor (0.314x) | $52,359 |
| BTC collateral per $10k face | 0.089955 BTC |

## Collateral and Covenant

See [common-parameters.md](common-parameters.md) for:
- Collateral ratio (150%)
- USD Reserve Fund (15% of face)
- Five collateral thresholds (Comfort through Emergency)
- Liquidation waterfall (mechanical, no discretion)
- Custodian requirements
- Price reference (CME CF Bitcoin Reference Rate)

## Yield Source

1. USD Reserve Fund (years 1-3)
2. Refinancing against appreciated collateral (year 3+)

The fixed coupon is sized at K * BFR at issuance and does not change. The issuer's obligation is constant. The collateral's floor value grows structurally, widening the issuer's margin every year.

## Mandatory Disclosures

1. The power law model could break. 15 years of data is not certainty.
2. Out-of-sample R2 = 0.546. The model explains half the variance in unseen data.
3. Under beta drift (5.688 to 5.50), BFR crosses below 4% by 2045.
4. 85% probability of at least one floor breach over 30 years (Poisson model).
5. The floor is definition-dependent. This product uses floor_current (0.432x) for operative calculations and floor_conservative (0.314x) for stress testing.

---

*Floor Bond Protocol. Open Source. MIT License.*
*Bitcoin Power Law Observatory. btcpowerlaw.nl.*
