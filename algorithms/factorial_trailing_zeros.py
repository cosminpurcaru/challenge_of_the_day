"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number. 
(You're not meant to calculate the factorial. Find another way to find the number of zeros.)

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...



Examples

zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 11! = 39916800 --> 2 trailing zeros
"""


def factorial_trailing_zeros(n):
    if n < 5:
        return 0
    trailing_zeros = 0
    exponent = 5
    while (n/exponent >= 1):
        trailing_zeros += int(n/exponent)
        exponent *= 5
    return trailing_zeros
