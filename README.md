# The Floor Bond Protocol

**Open source Bitcoin-backed fixed income. MIT License.**

Bitcoin's chaos above. Your yield below.

---

## What This Is

The Floor Bond is a senior secured debt instrument backed by Bitcoin collateral, with coupons paid from the structural growth of Bitcoin's power law floor. A mechanical covenant and independent trustee manage all collateral decisions. No human discretion. No model dependency after issuance.

This repository contains the complete protocol specification, 12 product variants, reference tools, and the research that validates the structure. Everything is public, reproducible, and auditable.

## The Submarine

A submarine operates below the ocean surface. Storms, waves, and surface chaos have no effect on it.

A Floor Bond lives below Bitcoin's power law floor. All of Bitcoin's famous volatility happens above the floor. The bond structure never surfaces. The collateral covenant, the liquidation waterfall, the USD reserve, and the tranche structure all operate in the calm water below.

The volatility that makes Bitcoin terrifying to institutions is the same volatility that makes Floor Bonds profitable. Every surge above the floor increases collateral value. Every return to trend widens the margin.

## The Numbers

All numbers use the exact compound BFR formula, pinned to January 1, 2027 issuance.

| Metric | Value |
|--------|-------|
| Bitcoin Floor Rate (BFR) | 36.0% annually, decelerating |
| Senior coupon (K=0.20) | 7.2% fixed |
| Junior coupon (K=0.35) | 12.6% fixed |
| Senior vs 5yr Treasury spread | +270 basis points |
| Senior leverage ceiling (year 10) | 50-100x practical |
| Conservative floor breaches (post-2010) | 0 |
| Backtest: safe-zone loan failures | 0 / 1,982 |

## Product Shelf (12 Instruments)

### Coupon-Bearing

| Product | Tranche | Term | Coupon |
|---------|---------|------|--------|
| Series F5-A | Senior | 5yr fixed | 7.2% |
| Series F5-B | Junior | 5yr fixed | 12.6% |
| Series F10-A | Senior | 10yr fixed | 7.2% |
| Series F10-B | Junior | 10yr fixed | 12.6% |
| Series V-A | Senior | Perpetual variable | 20% of BFR |
| Series V-B | Junior | Perpetual variable | 35% of BFR |

### Zero-Coupon (per $10,000 face)

| Product | Purchase Price | Implied Yield |
|---------|---------------|---------------|
| ZC-F5-A (Senior, 5yr) | $7,355 | 6.3% |
| ZC-F5-B (Junior, 5yr) | $5,910 | 11.1% |
| ZC-F10-A (Senior, 10yr) | $5,686 | 5.8% |
| ZC-F10-B (Junior, 10yr) | $3,798 | 10.2% |

Full specs in [`/specs`](specs/).

## How It Works

**Collateral.** 150% of face value in Bitcoin, held by an independent custodian (Coinbase Custody, Fidelity Digital Assets, or BitGo Trust).

**Tranching.** 70% senior / 30% junior. Junior absorbs all first losses. Senior has first-priority claim on liquidation proceeds.

**Coupon source.** The Bitcoin floor grows at 36% annually (decelerating). A fraction (K=0.20 for senior, K=0.35 for junior) is paid as coupon. The remainder stays as issuer margin.

**Covenant.** Five collateral thresholds (Comfort, Watch, Warning, Danger, Emergency) monitored daily at the CME CF Bitcoin Reference Rate. Emergency triggers an automatic liquidation waterfall. No human discretion.

**Reserve.** 15% of face value in US Treasuries (~4.5%). Services coupon payments years 1-3 without touching Bitcoin collateral.

## The Leverage Finding

After year 2, the power law floor exceeds the senior tranche's first-loss price under even the most conservative floor definition. The mathematical leverage ceiling becomes unbounded. The practical ceiling (including a 40% execution gap and 5% slippage) reaches 50-100x by year 10.

The leverage capacity of the senior tranche is not constrained by mathematics. It is constrained by regulation.

## Repository Structure

```
whitepaper/          The definitive document (v0.7)
specs/               12 product specs + common parameters + waterfall + tranche mechanics
research/            Claims registry, beta drift, reflecting barrier, 1.6x rule backtest, data reference
tools/               Reference implementations (Python)
  coupon_calculator.py
  leverage_analyzer.py
  zero_coupon_pricer.py
examples/            Executive summary for email/LinkedIn
data/                Power law parameters
```

## Quick Start

```bash
# Compute coupons for any issuance date
python tools/coupon_calculator.py --date 2027-01-01

# Analyze senior tranche leverage
python tools/leverage_analyzer.py --issuance 10000000

# Price zero-coupon variants
python tools/zero_coupon_pricer.py --terms 3 5 7 10
```

## Research Foundation

The Floor Bond Protocol is built on the Bitcoin Power Law Observatory's formally verified research stack.

| Finding | Result | Source |
|---------|--------|--------|
| Power law R2 (in-sample) | 0.956 | Paper 5, GPD Phase 1 |
| Power law R2 (out-of-sample) | 0.546 | Scanner S097 |
| Effective sample size | ~24 independent observations | GPD Phase 1 |
| Conservative floor (0.314x) post-2010 breaches | 0 | Scanner S001/R042 |
| Reflecting barrier truncation | 81%, chi2=203.9 | GPD Phase 1 |
| Volatility decay per cycle | ~21% (P1-P50) | Analysis, z=-5.28 |
| 1.6x Floor Rule failures in safe zone | 0 / 1,982 | Scanner INV-11 |
| Actuarially fair K-factors | 0.20 (senior), 0.35 (junior) | F004 derivation |

Full research papers at [btcpowerlaw.nl/research](https://btcpowerlaw.nl/research).

## What This Is Not

This is not investment advice. This is not a securities offering. This is not a prospectus.

This is an open source protocol specification. The first issuer to bring Floor Bonds to market captures the institutional Bitcoin fixed-income category. The protocol is free. The implementation advantage is execution speed, regulatory clearance, and distribution.

## Known Limitations

1. The power law model could break. 15 years is not 150 years.
2. Out-of-sample R2 is 0.546, not 0.956. The model explains half the variance in unseen data.
3. Volatility decay confidence intervals span zero per individual halving transition.
4. Under beta drift (5.688 to 5.50), the BFR crosses below 4% by 2045 instead of 2151.
5. Poisson model estimates 85% probability of at least one floor breach over 30 years.
6. No live issuances exist. This is infrastructure, not a track record.

## License

MIT. Use it. Build on it. Issue bonds with it.

## Contact

Scale Invariant Capital BV
[btcpowerlaw.nl](https://btcpowerlaw.nl)

---

*The Floor Bond Protocol is an open source financial instrument specification. Consult qualified legal counsel before issuing any securities in any jurisdiction.*
