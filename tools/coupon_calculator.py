#!/usr/bin/env python3
"""
Floor Bond Coupon Calculator
Reference implementation for the Floor Bond Protocol

Usage:
    python coupon_calculator.py                    # defaults (Jan 2027, K=0.20/0.35)
    python coupon_calculator.py --date 2028-01-01  # custom issuance date
    python coupon_calculator.py --k-senior 0.25    # custom K factor

Repository: github.com/JohnnyBCash/floor-bond-protocol
License: MIT
"""

import argparse
from datetime import datetime, timedelta

GENESIS = datetime(2009, 1, 3)
LOG_A = -16.493
BETA = 5.688

def days_since_genesis(date):
    return (date - GENESIS).days

def trend_price(date):
    import math
    d = days_since_genesis(date)
    return 10 ** (LOG_A + BETA * math.log10(d))

def floor_price(date, mult=0.432):
    return mult * trend_price(date)

def bfr_exact(date):
    d = days_since_genesis(date)
    return ((d + 365) / d) ** BETA - 1

def main():
    parser = argparse.ArgumentParser(description="Floor Bond Coupon Calculator")
    parser.add_argument("--date", default="2027-01-01", help="Issuance date (YYYY-MM-DD)")
    parser.add_argument("--k-senior", type=float, default=0.20, help="Senior K-factor")
    parser.add_argument("--k-junior", type=float, default=0.35, help="Junior K-factor")
    parser.add_argument("--face", type=float, default=10000, help="Face value per unit")
    args = parser.parse_args()

    issue = datetime.strptime(args.date, "%Y-%m-%d")
    bfr = bfr_exact(issue)
    trend = trend_price(issue)
    fl_current = floor_price(issue, 0.432)
    fl_conservative = floor_price(issue, 0.314)

    sr_coupon = args.k_senior * bfr
    jr_coupon = args.k_junior * bfr

    print(f"Floor Bond Coupon Calculator")
    print(f"{'='*50}")
    print(f"Issuance date:     {args.date}")
    print(f"Days since genesis: {days_since_genesis(issue)}")
    print(f"Trend price:       ${trend:,.0f}")
    print(f"Floor (0.432x):    ${fl_current:,.0f}")
    print(f"Floor (0.314x):    ${fl_conservative:,.0f}")
    print(f"BFR (exact):       {bfr:.2%}")
    print()
    print(f"Senior (K={args.k_senior:.2f}): {sr_coupon:.2%} = ${sr_coupon * args.face:,.0f}/yr per ${args.face:,.0f} face")
    print(f"Junior (K={args.k_junior:.2f}): {jr_coupon:.2%} = ${jr_coupon * args.face:,.0f}/yr per ${args.face:,.0f} face")
    print()

    # BFR schedule for bond lifetime
    print(f"BFR Deceleration Schedule:")
    print(f"{'Year':>4} {'Date':<12} {'BFR':>8} {'Floor(0.432x)':>14} {'Sr Cpn':>8} {'Jr Cpn':>8}")
    print("-" * 58)
    for yr in range(0, 11):
        dt = issue + timedelta(days=365 * yr)
        b = bfr_exact(dt)
        fl = floor_price(dt, 0.432)
        print(f"{yr:>4} {dt.strftime('%Y-%m-%d'):<12} {b:>7.1%} ${fl:>13,.0f} {args.k_senior*b:>7.1%} {args.k_junior*b:>7.1%}")

if __name__ == "__main__":
    main()
