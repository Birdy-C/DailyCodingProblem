'''
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
'''
# The time complexity of this brute force approach is on the order of x / y, which can be very high, for example if x is 2^31 - 1 and y is 1.
# https://www.dailycodingproblem.com/solution/88?token=e5c68f9e1a44d076659f36f358ebaab1b777840dcab25b7ba4dd0164d31e35a61f7cca55
'''
x = 31, y = 3 => x = 1001, y = 0011
11111 - 0011 <<3 = 0111, quotient = 1<<3
0111 - 0011<<1 = 0001, quotient = 1<<3 + 1<<1
1<<3 + 1<<1 = 1010 = 10
'''
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('division by zero')

    quotient = 0
    power = 32           # Assume 32-bit integer
    yPower = y << power  # Initial y^d value is y^32
    remainder = x        # Initial remainder is x
    while remainder >= y:
        while yPower > remainder:
            yPower >>= 1
            power -= 1
        quotient += 1 << power
        remainder -= yPower

    return quotient
