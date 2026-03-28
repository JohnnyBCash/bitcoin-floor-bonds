# Floor Bond Protocol: Claims Registry

All structural claims used in the Floor Bond Protocol, with verification status and source references.

## Core Statistical Claims

| # | Claim | Value | Status | Source |
|---|-------|-------|--------|--------|
| C1 | Power law R2 (in-sample) | 0.956 | Verified | Paper 5, GPD Phase 1 |
| C2 | Power law R2 (out-of-sample) | 0.546 | Verified | Scanner S097 |
| C3 | ADF stationarity (p-value) | 0.006 | Verified | Paper 5 |
| C4 | Effective sample size | ~24 independent observations | Verified | GPD Phase 1, autocorrelation analysis |
| C5 | Conservative floor (0.314x) breaches post-2010 | 0 | Verified | Scanner S001/R042 |
| C6 | Current floor (0.432x) breaches post-2010 | 0 | Verified | Scanner S001 |
| C7 | Reflecting barrier truncation | 81% deficit, chi2 = 203.9 | Verified | GPD Phase 1 |
| C8 | Left-tail KS statistic ratio | 6.3x full distribution | Verified | Raw data analysis |

## Floor Bond Specific Claims

| # | Claim | Value | Status | Source |
|---|-------|-------|--------|--------|
| F1 | BFR (Jan 2027, exact compound) | 36.0% | Verified | Exact formula: ((6572+365)/6572)^5.688 - 1 |
| F2 | Senior coupon (K=0.20) | 7.2% | Derived | K * BFR = 0.20 * 36.0% |
| F3 | Junior coupon (K=0.35) | 12.6% | Derived | K * BFR = 0.35 * 36.0% |
| F4 | 1.6x Floor Rule safe-zone failures | 0 / 1,982 | Verified | Scanner INV-11 |
| F5 | Senior vs 5yr Treasury spread | +270 bps | Derived | 7.2% - 4.5% |
| F6 | Volatility decay per cycle | ~21% (P1-P50) | Verified | Analysis, z = -5.28 |
| F7 | Beta drift: BFR below 4% | By 2045 (beta 5.688 -> 5.50) | Stress test | F004 corrected analysis |
| F8 | Poisson floor breach probability | 85% over 30 years | Model estimate | Whitepaper Section 11 |
| F9 | Maximum K_senior before margin negative | 0.30 (10yr, beta drift) | Stress test | F004 derivation |
| F10 | Actuarially fair K-factors | 0.20 senior, 0.35 junior | Derived | F004 with 30% uncertainty haircut |

## Zero-Coupon Claims

| # | Claim | Value | Status | Source |
|---|-------|-------|--------|--------|
| Z1 | ZC-F5-A purchase price | $7,355 per $10,000 face | Derived | Implied yield 6.3% |
| Z2 | ZC-F5-B purchase price | $5,910 per $10,000 face | Derived | Implied yield 11.1% |
| Z3 | ZC-F10-A purchase price | $5,686 per $10,000 face | Derived | Implied yield 5.8% |
| Z4 | ZC-F10-B purchase price | $3,798 per $10,000 face | Derived | Implied yield 10.2% |

## Verification Methods

1. **Scanner verification**: Automated code that runs against the full dataset (5,713 daily observations, 2010-07-18 to 2026-03-08)
2. **GPD Phase 1**: Generalized Pareto Distribution analysis of tail behavior
3. **F004 derivation**: Actuarial coupon pricing memo with corrected beta drift
4. **Raw data analysis**: Direct statistical tests on price residuals

## Data Sources

- Dataset: btcpowerlaw.nl/datasets/btc_historical.json
- Observations: 5,713 daily closes
- Period: 2010-07-18 to 2026-03-08
- Power law parameters: logA = -16.493, beta = 5.688, genesis = 2009-01-03

---

*Floor Bond Protocol. Open Source. MIT License.*
