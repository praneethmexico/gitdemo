#!/usr/bin/env python3
"""
Generate 10 random numbers and print their sum.
"""

import random


def main():
    nums = [random.random() for _ in range(10)]
    total = sum(nums)
    print("Numbers:", ", ".join(f"{n:.6f}" for n in nums))
    print(f"Sum: {total:.6f}")


if __name__ == "__main__":
    main()
