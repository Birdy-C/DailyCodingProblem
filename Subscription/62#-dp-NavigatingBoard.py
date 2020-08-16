'''
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''
def waysOfWalking(N, M):
    dp = [1 for _ in range(M)]
    for i in range(1, N):
        dpnew = dp.copy()
        for j in range(1, M):
            dpnew[j] = dpnew[j-1] + dp[j]
        dp = dpnew.copy()
    return dp[-1]
print(waysOfWalking(5,5))

# Recurrent
def waysOfWalkingRec(N, M):
    if N==0 or M==0:
        return 1
    return waysOfWalkingRec(N-1, M) + waysOfWalkingRec(N, M-1)
