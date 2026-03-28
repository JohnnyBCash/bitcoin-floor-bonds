# Beta Drift Analysis

## Summary

Beta drift is the risk that the power law exponent (currently 5.688) decreases over time, reducing the Bitcoin Floor Rate and narrowing the issuer's margin. This analysis quantifies the impact of beta drift on the Floor Bond Protocol.

## The Question

If beta drifts from 5.688 to 5.50 (a 3.3% decline), what happens to:
1. The floor growth rate (BFR)?
2. The issuer's cumulative margin?
3. The maximum sustainable K-factor?

## Corrected Analysis

### The Incorrect Result (F004 v2)

An earlier version of the analysis incorrectly computed an 80% floor drop under beta drift. This was caused by applying the drift to the absolute floor level rather than the growth rate. The error was identified and corrected.

### The Correct Result

Beta drift from 5.688 to 5.50 produces:
- **Floor level change**: -16% (not -80%)
- **BFR impact**: Gradual deceleration; BFR crosses below 4% by 2045 instead of 2151
- **Margin impact**: Issuer margin compressed but positive through year 10 at K=0.20

### The Pivot-Point Intuition

The floor level depends on `10^(logA + beta * log10(days))`. A small change in beta has a multiplicative effect that grows with time. At the reference date (6,572 days), the sensitivity is moderate. At 20,000 days (2063), the sensitivity is severe.

## Ten-Year Drift Table (Jan 2027 Issuance)

| Year | Beta=5.688 BFR | Beta=5.50 BFR | Difference |
|------|----------------|---------------|------------|
| 0 | 36.0% | 34.6% | -1.4% |
| 1 | 33.8% | 32.5% | -1.3% |
| 2 | 31.9% | 30.7% | -1.2% |
| 3 | 30.2% | 29.0% | -1.2% |
| 5 | 27.2% | 26.2% | -1.0% |
| 7 | 24.8% | 23.8% | -1.0% |
| 10 | 22.0% | 21.1% | -0.9% |

## Maximum Sustainable K-Factor

Under beta = 5.50, the maximum K_senior before the issuer's cumulative margin turns negative over 10 years is **0.30**. The recommended K=0.20 provides 50% headroom.

## Implications for the Floor Bond Protocol

1. Fixed-coupon products (F5, F10) are locked at issuance and unaffected by subsequent drift
2. Variable-coupon products (V-A, V-B) track BFR and would deliver lower coupons under drift
3. The 2-year lag in variable coupons provides a buffer against sudden drift
4. K=0.20 is conservative enough to survive the stress scenario with positive margin
5. Beta drift is the primary long-term structural risk to the protocol

## Mandatory Disclosure

Beta drift is disclosed in every product spec (Mandatory Disclosure item 3): "Under beta drift (5.688 to 5.50), BFR crosses below 4% by 2045."

---

*Floor Bond Protocol. Open Source. MIT License.*
