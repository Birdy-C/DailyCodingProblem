'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def largestSum(list):
    cache = [0 for i in range(len(list)+1)]
    cache[1] = list[0]
    for i in range(2, len(list)+1):
        cache[i] = max(list[i-1]+cache[i-2], cache[i-1])
    return cache[len(list)]

def largestSum_N(list):
    cache = [0, list[0]]
    for i in range(1, len(list)):
        cache[0], cache[1] = cache[1], max(list[i]+cache[0], cache[1])
    return cache[1]

a = [2, 4, 6, 2, 5]
b = [5, 1, 1, 5]
print(largestSum_N(a))
