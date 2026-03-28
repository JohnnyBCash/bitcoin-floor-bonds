# Floor Bond Whitepaper Changelog

## v0.7 (March 2026)
- Refinancing risk model added (Section 2.5): SOFR+200 base case, three stress scenarios, combined worst case, explicit break conditions
- "Self-liquidating" language refined to "structurally self-liquidating (via refinancing-supported repayment)"
- Fiat-side risks section added (Section 5.6): prime broker margin calls, MTM accounting, exit liquidity
- Effective sample size corrected to ~24 throughout (was ~200)
- "Structural" replaced with "empirical" for power law model descriptions
- MicroStrategy parallel softened to "directionally similar"
- Three independent LLM reviews incorporated (Grok 8.5/10, Gemini B+, ChatGPT A- 88/100)

## v0.6 (March 2026)
- F004 actuarial coupon derivation added: K=0.20 senior (7.2%), K=0.35 junior (12.6%)
- BFR corrected to exact compound formula: 36.0% at Jan 2027 (was 31.6% simplified)
- Beta drift stress test: 16% floor drop (corrected from 80% error in F004 v1)
- Raw data analysis: KS test, chi-squared, near-floor temporal distribution
- Full 1.6x backtest on raw data: 0/1,719 at <=1.4x
- Face value standardized to $10,000
- Reflecting barrier updated to 81% (was 63%)
- Zero-coupon variant added
- Noteholder breakeven analysis added
- Leverage analysis added (practical ceiling table)
- Four-layer disclosure framework added
- Product launch sequencing added

## v0.5 (March 2026)
- Three-reviewer round: Grok, Gemini, ChatGPT
- Adoption stall indicators section scoped
- Quarterly monitoring dashboard concept

## v0.4 (March 2026)
- First LLM peer review (Grok B+/A-)
- Presentation fixes applied

## v0.3 (March 2026)
- Tranching added: 70% senior / 30% junior
- Worked stress scenario (60% price drop)
- USD Reserve Fund (15% of face)
- Liquidation waterfall specified
- Three yield sources documented

## v0.2 (March 2026)
- Initial protocol specification
- MIT license
- Series F5, F10, V defined
- Collateral mechanics
- Five threshold levels
