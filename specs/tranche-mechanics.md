# Tranche Mechanics

## Structure

Every Floor Bond issuance is split into two tranches from the same collateral pool.

| Tranche | Share | Designation | Claim Priority |
|---------|-------|-------------|----------------|
| Senior | 70% | Series A | First |
| Junior | 30% | Series B | Residual |

The 70/30 split is the protocol recommendation. Issuers may adjust based on market conditions. The collateral mechanics are identical regardless of ratio.

## How Tranching Works

### Same Collateral, Different Risk

Both tranches are backed by the same Bitcoin collateral pool (150% of total face value). The difference is the claim priority in a liquidation event.

Senior noteholders are paid first. They take zero losses until the junior tranche is completely wiped out AND the remaining collateral is still insufficient.

Junior noteholders absorb all first losses. In exchange, they receive a higher coupon (K=0.35 vs K=0.20, a 1.75x premium).

### When Junior Is Wiped Out

For a $10M issuance ($7M senior, $3M junior) with 89.96 BTC collateral:

Junior is wiped when collateral value drops below total face value:
- Junior wipeout price: $111,166 (66.7% of issuance trend price)

Senior takes first loss when collateral drops below senior face value:
- Senior first-loss price: $77,816 (46.7% of issuance trend price)

The gap between $111,166 and $77,816 is the junior's absorption buffer. BTC must fall an additional 30% below the junior wipeout point before senior is impacted.

### The Leverage Implication

Because junior absorbs first losses, the senior tranche has built-in leverage protection. Combined with overcollateralization (150%) and the structural floor growth, the senior tranche's mathematical leverage ceiling becomes unbounded after year 2.

See [leverage analysis in the whitepaper] for the full table.

## K-Factor Allocation

| Tranche | K-Factor | Coupon (Jan 2027) | Rationale |
|---------|----------|-------------------|----------|
| Senior | 0.20 | 7.2% | Conservative. Retains 80% of floor growth as issuer margin. |
| Junior | 0.35 | 12.6% | Alpha = 1.75x senior. Compensates first-loss position. |

The alpha (K_junior / K_senior = 1.75) is calibrated so the junior coupon adequately compensates the additional risk. Under the beta drift stress scenario (beta = 5.50), the maximum K_senior before the issuer's cumulative margin turns negative over 10 years is 0.30. The recommended 0.20 provides 50% headroom.

## Noteholder Breakeven

Both tranches beat US Treasuries at their respective K-factors:

| Tranche | Coupon | vs 5yr Treasury (4.5%) | Spread |
|---------|--------|----------------------|--------|
| Senior | 7.2% | Beats by 270bps | +2.7% |
| Junior | 12.6% | Beats by 810bps | +8.1% |

For Series V (variable), the senior coupon crosses below 4.5% at approximately year 10. The junior coupon maintains the advantage for approximately 29 years.

## Why Two Tranches Instead of One

A single-tranche bond at K=0.25 would offer ~9% coupon. Splitting into senior and junior achieves three things:

1. The senior tranche becomes safe enough for regulated institutional capital (pension funds, insurance). These buyers cannot hold a single-tranche Bitcoin-backed instrument regardless of yield.

2. The junior tranche offers a high-yield product for crypto-native capital that already understands and accepts Bitcoin volatility risk.

3. The leverage capacity of the senior tranche (unbounded after year 2) enables institutional strategies that a single-tranche product cannot support.

The tranching is not financial engineering for its own sake. It is the mechanism that translates Bitcoin's structural properties into instruments that fit existing institutional mandates.

---

*Floor Bond Protocol. Open Source. MIT License.*
