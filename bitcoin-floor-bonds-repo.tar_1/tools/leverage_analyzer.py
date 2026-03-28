#!/usr/bin/env python3
"""
Floor Bond Senior Tranche Leverage Analyzer
Reference implementation for the Floor Bond Protocol

Computes mathematical and practical leverage ceilings for the
senior tranche at each year of a bond's lifetime.

Usage:
    python leverage_analyzer.py                        # defaults
    python leverage_analyzer.py --issuance 100000000   # $100M issuance
    python leverage_analyzer.py --execution-gap 0.50   # 50% worst-case drop

Repository: github.com/JohnnyBCash/floor-bond-protocol
License: MIT
"""

import argparse
from datetime import datetime, timedelta
import math

GENESIS = datetime(2009, 1, 3)
LOG_A = -16.493
BETA = 5.688

def days_since_genesis(date):
    return (date - GENESIS).days

def trend_price(date):
    d = days_since_genesis(date)
    return 10 ** (LOG_A + BETA * math.log10(d))

def floor_price(date, mult=0.432):
    return mult * trend_price(date)

def main():
    parser = argparse.ArgumentParser(description="Senior Tranche Leverage Analyzer")
    parser.add_argument("--date", default="2027-01-01", help="Issuance date")
    parser.add_argument("--issuance", type=float, default=10_000_000, help="Total issuance USD")
    parser.add_argument("--senior-pct", type=float, default=0.70, help="Senior tranche %")
    parser.add_argument("--collateral-ratio", type=float, default=1.50, help="Collateral ratio")
    parser.add_argument("--execution-gap", type=float, default=0.40, help="Worst-case daily drop")
    parser.add_argument("--slippage", type=float, default=0.05, help="Liquidation slippage")
    args = parser.parse_args()

    issue = datetime.strptime(args.date, "%Y-%m-%d")
    btc_price = trend_price(issue)
    senior_face = args.issuance * args.senior_pct
    btc_collateral = (args.issuance * args.collateral_ratio) / btc_price
    senior_loss_price = senior_face / btc_collateral

    print(f"Senior Tranche Leverage Analyzer")
    print(f"{'='*70}")
    print(f"Issuance: ${args.issuance:,.0f} | Senior: ${senior_face:,.0f} ({args.senior_pct:.0%})")
    print(f"BTC at trend: ${btc_price:,.0f} | Collateral: {btc_collateral:.2f} BTC")
    print(f"Senior first-loss price: ${senior_loss_price:,.0f}")
    print(f"Execution gap: {args.execution_gap:.0%} | Slippage: {args.slippage:.0%}")
    print()

    print(f"{'Year':>4} {'Floor(cons)':>12} {'Floor(curr)':>12} {'Math Lev':>10} {'Practical':>10} {'Recommended':>12}")
    print("-" * 62)

    for yr in range(0, 11):
        dt = issue + timedelta(days=365 * yr)
        fl_cons = floor_price(dt, 0.314)
        fl_curr = floor_price(dt, 0.432)

        # Mathematical leverage
        collat_at_cons = btc_collateral * fl_cons
        if collat_at_cons >= senior_face:
            math_lev = "INF"
        else:
            loss = 1 - collat_at_cons / senior_face
            math_lev = f"{1/loss:.1f}x"

        # Practical leverage (with execution gap and slippage)
        after_gap = fl_cons * (1 - args.execution_gap)
        after_slip = after_gap * (1 - args.slippage)
        collat_practical = btc_collateral * after_slip
        if collat_practical >= senior_face:
            prac_lev = "INF"
            rec = "20-50x" if yr >= 4 else ("10-20x" if yr >= 3 else ("3-5x" if yr >= 2 else ("2-3x" if yr >= 1 else "1x")))
        else:
            loss_p = 1 - collat_practical / senior_face
            prac_val = 1 / loss_p
            prac_lev = f"{prac_val:.1f}x"
            rec = f"{max(1, prac_val * 0.5):.0f}x"

        print(f"{yr:>4} ${fl_cons:>11,.0f} ${fl_curr:>11,.0f} {math_lev:>10} {prac_lev:>10} {rec:>12}")

if __name__ == "__main__":
    main()
