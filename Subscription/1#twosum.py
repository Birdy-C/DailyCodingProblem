def two_sum_brute(lis, k):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if i != j and lis[i] + lis[j] == k:
                return True
    return False

def two_sum_set(lis, k):
    seen = Set()
    for i in range(len(lis)):
        if k - lis[i] in seen:
            return True
        seen.add(lis[i])
    return False

from bisect import bisect_left
# bisect_left(a, x, lo=0, hi=len(a))  insertion would be to the left of existing entries
# bisect_right(a, x, lo=0, hi=len(a))  insertion would be to the right of existing entries

def binary_search(lis, x):
    lo = 0
    hi = len(lis)
    index = bisect_left(lis, x, lo, hi)
    return index if 0 <= index < hi and lis[index] == x else -1

def two_sum_bin(lis, k):
    lis.sort()
    for i in range(len(lis)):
        target = binary_search(lis, k - lis[i])
        if target != -1 and target != i:
            return True
    return False

a = [1,2,3,3,4,5,6,5,5,7,7]
print(two_sum_bin(a, 14))

dic = [(x, i) for i, x in enumerate(a)]
print(dic)
