'''
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''
# 0 1 2 3 4 5
# 1 1 2 3 5
def climbingStairs(N, X):
    cache = [0 for i in range(N+1)]
    cache[0] = 1
    for i in range(1, N+1):
        for step in X:
            if i - step >= 0:
                cache[i] += cache[i - step]
    return cache[N]

print(climbingStairs(5, [1,2]))
