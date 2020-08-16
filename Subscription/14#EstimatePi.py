'''
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''
# Note that this doesn't give a perfect approximation -- we need more iterations to get a closer estimate. We want the digits of pi up to 3 decimal places. This translates to an error of < 10^(-3). The error scales with the square root of the number of guesses, which means we need 10^6 iterations to get to our desired precision. If we want more precision, we'll have to crank up the iterations.
# Extra credit: make this program multi-process.
from random import uniform
from math import pow

def generate():
    return (uniform(-1,1), uniform(-1,1))

def is_in_circle(cord):
    return cord[0]*cord[0] + cord[1]*cord[1] <= 1.0

def estimate():
    num_iter = 10000000
    in_circle = 0
    for _ in range(num_iter):
        if is_in_circle(generate()):
            in_circle += 1
    return in_circle / num_iter * 4

print(estimate())
