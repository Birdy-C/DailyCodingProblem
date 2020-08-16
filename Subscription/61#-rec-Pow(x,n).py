'''
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''
# https://www.dailycodingproblem.com/solution/61?token=64f2c07bb6d46145dd5dea3775d73c5bfc2ba8a01a91063d50d4d6a842279ecf2624f808
def power(x, y):
    base = x
    exponent = y
    if y < 0:
        base = 1 / x
        exponent = -y
    coeff = 1
    while y > 1:
        if y % 2 == 0:
            base *= base
            y = y // 2
        else:
            coeff *= base
            base *= base
            y = (y - 1) // 2
    return coeff * base

def power(x, y):
    if y < 0:
        return power(1 / x, -y)
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return power(x * x, y // 2)
    else: # y is odd
        return x * power(x * x, y // 2)
