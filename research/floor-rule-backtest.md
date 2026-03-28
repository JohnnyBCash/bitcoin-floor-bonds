# 1.6x Floor Rule — Full Backtest

## Summary

The 1.6x Floor Rule states: a loan issued at or below 1.6x the conservative floor (0.314x trend) will not be liquidated at the Emergency threshold (collateral < 100% of face). This analysis backtests the rule against every daily close in the dataset.

## The Rule

For any issuance date where the BTC price is at or below 1.6x the conservative floor:
- Entry price <= 1.6 * 0.314 * trend_price
- Collateral ratio at issuance: 150%
- Emergency threshold: collateral < 100% of face

The rule predicts: no loan issued in the safe zone (<=1.6x) will ever trigger Emergency liquidation at any future date in the dataset.

## Dataset

| Parameter | Value |
|-----------|-------|
| Source | btcpowerlaw.nl/datasets/btc_historical.json |
| Observations | 5,713 daily closes |
| Period | 2010-07-18 to 2026-03-08 |
| Entries in safe zone (<=1.6x) | 1,982 |
| Entries at <=1.4x | 1,719 |

## Results

### At 1.6x Entry

| Metric | Value |
|--------|-------|
| Entries tested | 1,982 |
| Liquidation failures | 0 |
| Failure rate | 0.00% |

### At 1.4x Entry

| Metric | Value |
|--------|-------|
| Entries tested | 1,719 |
| Liquidation failures | 0 |
| Failure rate | 0.00% |

### LTV Sensitivity

| Entry Multiple | Entries | Failures | Failure Rate |
|----------------|---------|----------|--------------|
| <= 1.0x | 0 | 0 | N/A |
| <= 1.2x | 487 | 0 | 0.00% |
| <= 1.4x | 1,719 | 0 | 0.00% |
| <= 1.6x | 1,982 | 0 | 0.00% |
| <= 1.8x | 2,843 | 0 | 0.00% |
| <= 2.0x | 3,291 | 3 | 0.09% |

The first failures appear at entry multiples above 1.8x, all in cycle 1 (pre-2012).

## Floor Definition Sensitivity

| Floor Definition | Multiplier | Entries <=1.6x | Failures |
|------------------|-----------|----------------|----------|
| Conservative (full-dataset P1) | 0.314x | 1,982 | 0 |
| Current (C3-C4 rolling P1) | 0.432x | 3,847 | 0 |

Both floor definitions produce zero failures at the 1.6x threshold.

## Temporal Distribution of Failures

No failures occur in the safe zone across any halving cycle. The rule holds from the earliest testable date (2010-07-18) through the end of the dataset.

## Implications

1. The 1.6x rule provides a conservative entry criterion for Floor Bond issuance
2. Zero failures across 1,982 entries validates the collateral structure
3. The 150% collateral ratio at issuance places all bonds well within the safe zone
4. The result is robust to floor definition choice

## Caveats

- Backtests do not guarantee future performance
- The effective sample size is ~24 independent observations
- The dataset begins at 2010-07-18; pre-market behavior is untestable
- Intraday breaches (not captured by daily closes) could produce different results

---

*Floor Bond Protocol. Open Source. MIT License.*
