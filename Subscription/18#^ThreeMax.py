'''
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
                                   2
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
                                1        4
10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''
# This takes Nk time
def threeMaxNK(arr, K):
    buffer = [arr[i] for i in range(K)]
    cur = K-1
    for inx in range(K-1, len(arr)):
        buffer[cur] = arr[inx]
        print(max(buffer))
        cur = (cur+1) % K

# Changing the buffer to a max heap still takes Nlogk

# We use a monotone queue
from collections import deque
def threeMax(arr, K):
    q = deque()
    for i in range(K):
        while q and arr[q[-1]] < arr[i]:
            q.pop()
        q.append(i)
    for i in range(K, len(arr)):
        print(arr[q[0]])
        while q and q[0] <= i - K:
            q.popleft()
        while q and arr[q[-1]] < arr[i]:
            q.pop()
        q.append(i)
    print(arr[q[0]])


threeMax([10, 5, 2, 7, 8, 7], 3)
