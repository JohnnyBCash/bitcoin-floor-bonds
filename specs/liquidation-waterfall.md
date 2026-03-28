# Liquidation Waterfall

## Trigger

The liquidation waterfall executes automatically when the collateral ratio drops below 100% of total face value (Emergency threshold). No human discretion. No issuer input. No cure period.

## Execution Sequence

### Step 1: Sell
Trustee sells all pledged Bitcoin at the CME CF Bitcoin Reference Rate (New York Variant, published daily at 4:00 PM Eastern).

### Step 2: Pay Senior
100% of senior tranche principal plus all accrued and unpaid interest is paid first. Senior noteholders are made whole before any other distribution.

### Step 3: Pay Junior
Remaining proceeds after senior repayment go to junior noteholders. If proceeds cover 100% of junior principal plus accrued interest, junior is paid in full.

### Step 4: Residual to Issuer
Any surplus proceeds after both tranches are fully repaid go to the bond issuer.

### Step 5: Shortfall
If total proceeds are insufficient to cover senior principal in full, senior noteholders receive a pro-rata distribution of all available proceeds. Junior noteholders receive nothing.

## Execution Risk Factors

The waterfall fires at the daily reference rate but BTC can move between the trigger and actual sale.

| Risk Factor | Estimate | Mitigation |
|-------------|----------|------------|
| Execution gap (intraday move after trigger) | Up to -40% | Collateral ratio buffer above Emergency |
| Slippage ($10M position) | 0.5-2% | Multiple execution venues |
| Slippage ($100M+ position) | 5-10% | Staged execution over multiple sessions |
| Exchange downtime | Hours | Multi-venue custodian requirement |

## What the Waterfall Does Not Do

- It does not attempt to time the market.
- It does not partially liquidate (all-or-nothing at Emergency).
- It does not allow the issuer to delay, negotiate, or override.
- It does not depend on any model output after issuance. The reference rate is a market observation.

---

*Floor Bond Protocol. Open Source. MIT License.*
