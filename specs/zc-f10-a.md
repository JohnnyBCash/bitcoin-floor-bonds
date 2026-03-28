# Floor Bond ZC-F10-A (Senior, 10-Year Zero-Coupon)

## Product Summary

| Parameter | Value |
|-----------|-------|
| Product | ZC-F10-A |
| Tranche | Senior (70% of issuance) |
| Term | 10 years |
| Face value | $10,000 per unit |
| Coupon type | Zero-coupon (purchased at discount, redeemed at face) |
| K-factor | 0.20 |
| Purchase price | $5,686 per $10,000 face |
| Implied yield | 5.8% |
| Discount | 43.1% |
| Target buyer | Endowments, sovereign wealth, compounding mandates |

## Risk Profile

Investment grade equivalent. No periodic cash flow. Entire return from discount at purchase. Most overcollateralized instrument at maturity.

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

This is a zero-coupon instrument. No periodic coupon payments.

The noteholder's entire return comes from the discount at purchase. The issuer retains all floor growth during the bond's lifetime, using it to build collateral. The face value payment at maturity comes from the vastly appreciated collateral.

At maturity, the collateral's floor value far exceeds the face value obligation, making this the most overcollateralized instrument in the Floor Bond shelf.

## Mandatory Disclosures

1. The power law model could break. 15 years of data is not certainty.
2. Out-of-sample R2 = 0.546. The model explains half the variance in unseen data.
3. Under beta drift (5.688 to 5.50), BFR crosses below 4% by 2045.
4. 85% probability of at least one floor breach over 30 years (Poisson model).
5. The floor is definition-dependent. This product uses floor_current (0.432x) for operative calculations and floor_conservative (0.314x) for stress testing.

---

*Floor Bond Protocol. Open Source. MIT License.*
*Bitcoin Power Law Observatory. btcpowerlaw.nl.*
