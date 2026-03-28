# Data Reference

## Power Law Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| logA | -16.493 | Santostasi Bitcoin Power Law regression |
| beta | 5.688 | Santostasi Bitcoin Power Law regression |
| Genesis date | 2009-01-03 | Bitcoin network launch |

## Floor Definitions

| Name | Multiplier | Method | Use |
|------|-----------|--------|-----|
| Conservative | 0.314x | Full-dataset P1 | Stress testing, collateral thresholds |
| Published | 0.422x | Cycle 4 P1 | Legacy papers (pre-March 2026) |
| Current | 0.432x | C3-C4 rolling average P1 | Current operative definition |

## Formulas

### Trend Price
```
trend_price(date) = 10^(logA + beta * log10(days_since_genesis))
```

### Floor Price
```
floor_price(date) = multiplier * trend_price(date)
```

### Bitcoin Floor Rate (BFR) — Exact Compound
```
BFR(date) = ((days + 365) / days)^beta - 1
```
where `days = days_since_genesis(date)`.

**Do not use** the simplified approximation `beta * 365 / days`. It overestimates BFR at short timescales and underestimates at long timescales.

### Coupon Rate
```
coupon = K * BFR(issuance_date)
```
where K = 0.20 (senior) or K = 0.35 (junior).

## Reference Issuance: January 1, 2027

| Metric | Value |
|--------|-------|
| Days since genesis | 6,572 |
| BFR (exact compound) | 35.99% (~36.0%) |
| Trend price | $166,749 |
| Floor (0.432x current) | $72,036 |
| Floor (0.314x conservative) | $52,359 |
| Senior coupon (K=0.20) | 7.20% = $720/yr per $10,000 face |
| Junior coupon (K=0.35) | 12.60% = $1,260/yr per $10,000 face |
| BTC collateral per $10k face (150%) | 0.089955 BTC |

## Dataset

| Parameter | Value |
|-----------|-------|
| Source | btcpowerlaw.nl/datasets/btc_historical.json |
| Observations | 5,713 daily closes |
| Start | 2010-07-18 |
| End | 2026-03-08 |
| Effective sample size | ~24 independent observations |
| In-sample R2 | 0.956 |
| Out-of-sample R2 | 0.546 |

## Key Statistical Results

| Test | Result |
|------|--------|
| ADF stationarity (p-value) | 0.006 |
| KS left-tail ratio | 6.3x |
| Chi-squared (below-floor deficit) | 203.9 (81% truncation) |
| Volatility decay per cycle | ~21% (z = -5.28) |
| Safe-zone loan failures (1.6x rule) | 0 / 1,982 |

## BFR Deceleration Schedule (Jan 2027 Issuance)

| Year | Date | BFR | Senior (K=0.20) | Junior (K=0.35) |
|------|------|-----|-----------------|------------------|
| 0 | 2027-01-01 | 36.0% | 7.2% | 12.6% |
| 1 | 2028-01-01 | 33.8% | 6.8% | 11.8% |
| 2 | 2029-01-01 | 31.9% | 6.4% | 11.2% |
| 3 | 2030-01-01 | 30.2% | 6.0% | 10.6% |
| 5 | 2032-01-01 | 27.2% | 5.4% | 9.5% |
| 7 | 2034-01-01 | 24.8% | 5.0% | 8.7% |
| 10 | 2037-01-01 | 22.0% | 4.4% | 7.7% |

---

*Floor Bond Protocol. Open Source. MIT License.*
