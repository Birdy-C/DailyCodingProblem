'''
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''
'https://www.dailycodingproblem.com/solution/75?token=dda18a1f32e0c2b9923a4259f921c83e47365d53f42d499fb92484bdd6a3196185325e65'
# Recursive
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return 1

    max_ending_here = 0
    for i in range(len(arr)):
        ending_at_i = longest_increasing_subsequence(arr[:i])
        if arr[-1] > arr[i - 1] and ending_at_i + 1 > max_ending_here:
            max_ending_here = ending_at_i + 1
    return max_ending_here

# DP
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)
