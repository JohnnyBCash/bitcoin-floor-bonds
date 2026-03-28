#!/usr/bin/env python3
"""
Floor Bond Zero-Coupon Pricer
Reference implementation for the Floor Bond Protocol

Computes purchase prices for zero-coupon Floor Bonds across
all maturities and K-factors.

Usage:
    python zero_coupon_pricer.py                    # defaults
    python zero_coupon_pricer.py --terms 3 5 7 10   # custom terms
    python zero_coupon_pricer.py --face 100000      # custom face value

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

def bfr_exact(date):
    d = days_since_genesis(date)
    return ((d + 365) / d) ** BETA - 1

def main():
    parser = argparse.ArgumentParser(description="Zero-Coupon Floor Bond Pricer")
    parser.add_argument("--date", default="2027-01-01", help="Issuance date")
    parser.add_argument("--face", type=float, default=10000, help="Face (redemption) value")
    parser.add_argument("--terms", nargs="+", type=int, default=[3, 5, 7, 10], help="Maturity terms in years")
    parser.add_argument("--k-values", nargs="+", type=float, default=[0.15, 0.20, 0.25, 0.30, 0.35], help="K-factors")
    args = parser.parse_args()

    issue = datetime.strptime(args.date, "%Y-%m-%d")

    print(f"Zero-Coupon Floor Bond Pricer")
    print(f"{'='*70}")
    print(f"Issuance: {args.date} | Face value: ${args.face:,.0f}")
    print()

    # Header
    k_headers = "".join(f"{'K='+f'{k:.2f}':>12}" for k in args.k_values)
    print(f"{'Term':>6} {'BFR range':>14}{k_headers}")
    print(f"{'':>6} {'':>14}" + "".join(f"{'Price':>12}" for _ in args.k_values))
    print("-" * (22 + 12 * len(args.k_values)))

    for term in args.terms:
        bfr_start = bfr_exact(issue)
        bfr_end = bfr_exact(issue + timedelta(days=365 * term))
        bfr_avg = (bfr_start + bfr_end) / 2

        prices = []
        for k in args.k_values:
            implied_yield = k * bfr_avg
            price = args.face / (1 + implied_yield) ** term
            prices.append(price)

        price_str = "".join(f"${p:>11,.0f}" for p in prices)
        print(f"{term:>4}yr {bfr_start:.0%}-{bfr_end:.0%}{price_str:>}")

    print()

    # Detailed table for default K-factors (senior=0.20, junior=0.35)
    print(f"Product Summary (Senior K=0.20, Junior K=0.35):")
    print(f"{'Product':<30} {'Price':>10} {'Yield':>8} {'Discount':>10}")
    print("-" * 60)

    for term in args.terms:
        bfr_start = bfr_exact(issue)
        bfr_end = bfr_exact(issue + timedelta(days=365 * term))
        bfr_avg = (bfr_start + bfr_end) / 2

        for k, tranche in [(0.20, "Senior"), (0.35, "Junior")]:
            implied = k * bfr_avg
            price = args.face / (1 + implied) ** term
            discount = 1 - price / args.face
            label = f"ZC-F{term}-{tranche[0]} ({tranche}, {term}yr)"
            print(f"{label:<30} ${price:>9,.0f} {implied:>7.1%} {discount:>9.1%}")

if __name__ == "__main__":
    main()
