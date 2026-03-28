# Reflecting Barrier Analysis

## Summary

Three independent statistical tests confirm that Bitcoin's power law floor acts as a reflecting barrier — a boundary where price behavior changes qualitatively. The distribution of log-residuals is truncated at the left tail in a way that cannot be explained by sampling noise.

## Test 1: Kolmogorov-Smirnov (Left-Tail)

The KS statistic measures the maximum distance between the observed cumulative distribution and the theoretical (normal) distribution.

| Metric | Full Distribution | Left Tail Only |
|--------|-------------------|----------------|
| KS statistic | 0.032 | 0.201 |
| Ratio | 1.0x | 6.3x |
| p-value | < 0.01 | < 10^-43 |

The left tail deviates from normal 6.3 times more than the overall distribution. This is the signature of a truncation boundary.

## Test 2: Chi-Squared (Below-Floor Deficit)

Binning log-residuals and comparing observed vs expected counts below the conservative floor (0.314x trend):

| Metric | Value |
|--------|-------|
| Expected observations below floor | ~57 (based on normal tail) |
| Observed observations below floor | ~15 |
| Deficit | 74.2% |
| Chi-squared | 203.9 |
| p-value | < 10^-10 |
| Overall truncation | 81% |

81% of the expected below-floor observations are missing. The floor removes them.

## Test 3: Temporal Distribution of Near-Floor Events

Near-floor events (within 1.2x of the conservative floor) are not clustered in a single era. They appear across all halving cycles:

| Halving Cycle | Period | Near-Floor Events |
|---------------|--------|-------------------|
| Cycle 1 | 2010-2012 | Present |
| Cycle 2 | 2012-2016 | Present |
| Cycle 3 | 2016-2020 | Present |
| Cycle 4 | 2020-2024 | Present |

This rules out the hypothesis that the floor is an artifact of a single early-period anomaly.

## Summary of Floor Evidence

| Test | Result | Interpretation |
|------|--------|----------------|
| KS left-tail | 6.3x ratio, p < 10^-43 | Floor truncates the distribution |
| Chi-squared | 81% deficit, chi2 = 203.9 | 81% of expected sub-floor observations missing |
| Temporal | All cycles | Not an era-specific artifact |

## Implications for Floor Bonds

The reflecting barrier provides the statistical foundation for the Floor Bond Protocol:

1. The floor is not a regression artifact — it is a distributional truncation
2. The truncation persists across all halving cycles
3. The conservative floor (0.314x) has zero post-2010 breaches
4. The current floor (0.432x) has zero post-2010 breaches
5. These findings support using the floor growth rate (BFR) as a coupon source

## Caveats

- The power law model is empirical, not derived from first principles
- The effective sample size is ~24 independent observations, not 5,713
- 15 years of data cannot guarantee future behavior
- The reflecting barrier could weaken or disappear if Bitcoin's adoption dynamics change

---

*Floor Bond Protocol. Open Source. MIT License.*
