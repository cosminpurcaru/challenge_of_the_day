"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number. 
(You're not meant to calculate the factorial. Find another way to find the number of zeros.)

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...



Examples

# Input: n = 5
# Output: 1 (5! = 720)

# Input: n = 15
# Output: 3 (15! = 1307674368000)

# Input: n = 20
# Output: 4 (20! = 2432902008176640000)

# Input: n = 25
# Output: 5 (25! = 15511210043330985984000000)

# Input: n = 100
# Output: 24 (100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)
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
