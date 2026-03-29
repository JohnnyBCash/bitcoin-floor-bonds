# Floor Bond Protocol: Common Parameters

All Floor Bond instruments share these parameters. Product-specific parameters are in each product spec.

## Unit Economics

| Parameter | Value |
|-----------|-------|
| Face value | $10,000 per unit |
| Minimum purchase | 1 unit |
| Denomination | USD |

## Collateral Structure

| Parameter | Value |
|-----------|-------|
| Collateral asset | Bitcoin (BTC) |
| Collateral ratio at issuance | 150% of total face value |
| BTC quantity per unit | Face value * 1.50 / BTC price at issuance |
| Collateral custody | Coinbase Custody Trust, Fidelity Digital Assets, or BitGo Trust |
| Segregation | Per-issuance segregated wallet. Not commingled. |

## Tranche Structure

| Parameter | Value |
|-----------|-------|
| Senior tranche (Series A) | 70% of total issuance |
| Junior tranche (Series B) | 30% of total issuance |
| Senior priority | First claim on all liquidation proceeds |
| Junior role | Absorbs all first losses before senior is impacted |

## USD Reserve Fund

| Parameter | Value |
|-----------|-------|
| Size | 15% of total face value |
| Investment | Short-duration US Treasury obligations |
| Expected yield | ~4.5% annually |
| Purpose | Service coupon payments years 1-3 without touching BTC collateral |
| Custody | Held by trustee in segregated account |

## Price Reference

| Parameter | Value |
|-----------|-------|
| Reference rate | CME CF Bitcoin Reference Rate, New York Variant |
| Frequency | Daily, 4:00 PM Eastern |
| Use | All collateral valuations, covenant triggers, liquidation execution |

## Collateral Thresholds

| Level | Trigger (collateral/face) | Action |
|-------|--------------------------|--------|
| Comfort | >= 200% | No action |
| Watch | < 200%, >= 162% | Issuer notified. Daily monitoring. |
| Warning | < 162%, >= 130% | 14-day cure period. Issuer must add collateral. |
| Danger | < 130%, >= 100% | 48-hour margin call to restore 130%. |
| Emergency | < 100% | Immediate mechanical liquidation. |

## Liquidation Waterfall

When Emergency threshold is breached:

1. Trustee sells all pledged BTC at CME CF Bitcoin Reference Rate.
2. Senior principal and accrued interest paid first and in full.
3. Remaining proceeds to junior noteholders.
4. Residual after both tranches to issuer.
5. If insufficient for senior: pro-rata to senior. Junior receives nothing.

No human discretion at any step.

## Power Law Parameters

| Parameter | Value |
|-----------|-------|
| logA | -16.493 |
| beta | 5.688 |
| Genesis | 2009-01-03 |
| Floor definition (stress testing) | Conservative: 0.314x trend |
| Floor definition (operative) | Current: 0.432x trend |

## BFR Formula

```
BFR(date) = ((days_since_genesis + 365) / days_since_genesis) ^ 5.688 - 1
```

All coupon calculations use the exact compound formula. Do not use the simplified approximation (beta * 365 / days).

## License

MIT. Open source protocol. See LICENSE file.

## Disclaimers

The Floor Bond Protocol is an open source financial instrument specification. It is not investment advice, legal advice, or a securities offering. Consult qualified legal counsel before issuing any securities in any jurisdiction.
