'''
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''
# reservoir sampling! https://www.youtube.com/watch?v=A1iwzSew5QY

import random

def pick(stream):
    random_ele = None
    for i, ele in enumerate(stream):
        if random.randint(1, i+1) == i+1:
            random_ele = ele
    return random_ele
