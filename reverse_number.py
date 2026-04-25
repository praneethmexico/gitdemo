"""reverse_number.py
Simple CLI to reverse an integer's digits, preserving sign.
"""

def reverse_number(n: int) -> int:
    """Return the integer obtained by reversing the digits of n."""
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    rev = 0
    while n_abs:
        rev = rev * 10 + (n_abs % 10)
        n_abs //= 10
    return sign * rev


if __name__ == "__main__":
    try:
        s = input("Enter an integer: ").strip()
        n = int(s)
        print(reverse_number(n))
    except ValueError:
        print("Please enter a valid integer.")
