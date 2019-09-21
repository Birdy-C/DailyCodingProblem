'''
This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.
'''
'''
We can solve this problem by seeing that if we multiply x with b, it solves half the problem. Since we want y to behave in opposite, we can get the same behavior by multiplying y with (1 - b).

Now, (x * b) gives x when b is 1 and 0 otherwise. Similarly, (y * (1 - b)) gives y when b is 0 and 0 otherwise. We can just combine the two formulas with either a + or |,
'''
def switch(x, y, b):
  return (x * b) | (y * (1 - b))

def myswitch(x, y, b):
    s = 1 if b==1 else 0
    for i in range(32):
        b = b | s<<i
    return (b^y)&y | (~b^x)&x

print(myswitch(12, 45, 0))
