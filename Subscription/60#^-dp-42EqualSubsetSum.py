'''
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
'''
# Don't do it by calculating sum of powersets
def partition(s):
    k = sum(s)
    if k % 2 != 0:
        return False
    k_over_two = k // 2

    A = [[False for _ in range(len(s) + 1)] for _ in range(k_over_two + 1)]

    for j in range(len(s) + 1):
        A[0][j] = True

    for i in range(1, k_over_two + 1):
        A[i][0] = False

    for i in range(1, k_over_two + 1):
        for j in range(1, len(s) + 1):
            using_last = i - s[j - 1]
            if using_last >= 0:
                A[i][j] = A[i][j - 1] or A[using_last][j - 1]
            else:
                A[i][j] = A[i][j - 1]
    return A[-1][-1]
