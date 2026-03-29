# The Floor Bond Protocol
## Open Source Bitcoin-Backed Fixed Income

**Scale Invariant Capital BV | btcpowerlaw.nl | MIT License**

---

**The problem.** Bitcoin's $1.7 trillion market cap sits largely idle as collateral. No instrument separates Bitcoin's structural growth from its price volatility. Institutions cannot participate.

**The insight.** Bitcoin's price follows a power law with a mathematically verifiable floor. This floor has never been breached in 15 years of daily data (conservative definition, 0.314x trend). It grows at 36% annually, decelerating predictably. All volatility happens above the floor.

**The instrument.** The Floor Bond is a senior secured debt instrument backed by 150% Bitcoin collateral, with coupons paid from floor growth. An independent trustee manages a mechanical five-level covenant. No human discretion after issuance. Price reference: CME CF Bitcoin Reference Rate.

**The structure.** 70% senior tranche (first claim, 7.2% coupon) / 30% junior tranche (first loss, 12.6% coupon). 15% USD reserve in Treasuries covers years 1-3. Five collateral thresholds trigger automatic responses from Watch through Emergency liquidation.

**The product shelf.** 12 instruments: 6 coupon-bearing (F5, F10, and perpetual variable in senior/junior pairs) plus 4 zero-coupon variants. Senior yields beat 5-year Treasuries by 270 basis points. Junior by 810.

**The leverage finding.** After year 2, the power law floor exceeds the senior tranche's first-loss price under even the most conservative definition. Practical leverage ceiling: 50-100x by year 10. The constraint is regulatory, not mathematical.

**The validation.** Formal verification of six structural claims by two independent methods. Out-of-sample R2 = 0.546 (first published for any Bitcoin power law research). Reflecting barrier: 81% distribution truncation (chi2 = 203.9). Zero safe-zone loan failures across 1,982 entries. 100,000-path Monte Carlo stress test.

**The honest risk.** The power law could break. Effective sample size is ~24 independent observations. Under beta drift, BFR falls below 4% by 2045. Poisson model gives 85% probability of at least one floor breach over 30 years. All disclosed. No hiding.

**The opportunity.** The protocol is open source (MIT). The first issuer captures the institutional Bitcoin fixed-income category. Everything needed to issue is published: whitepaper, product specs, reference tools, research, and price data.

**Contact:** Scale Invariant Capital BV. btcpowerlaw.nl. floor-bond-protocol on GitHub.
