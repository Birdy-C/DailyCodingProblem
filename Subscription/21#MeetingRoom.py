'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''
# Using TreeMap
def maxOverlap_TreeMap(intervals):
    book = {}
    for start, end in intervals:
        book[start] =  1
        book[end]   = -1
    res, overlap = 0, 0
    a = sorted(book.items(), key=lambda obj: obj[0])
    print(a)
    for point, val in a:
        overlap += val
        res = max(res, overlap)
    return res

# Using Two pointers
def maxOverlap_TP(intervals):
    starts = sorted(start for start, end in intervals)
    ends   = sorted(end   for start, end in intervals)
    i, j = 0, 0
    res, overlap = 0, 0
    while j < len(ends) and i < len(starts):
        if starts[i] < ends[j]:
            i += 1
            overlap += 1
            res = max(res, overlap)
        else:
            j += 1
            overlap -= 1
    return res
# Simple iteration
def maxOverlap_TP1(intervals):
    starts = sorted(start for start, end in intervals)
    ends   = sorted(end   for start, end in intervals)
    res, j = 0, 0
    for i in range(len(intervals)):
        if starts[i] < ends[j]:
            res += 1
        else:
            j += 1
    return res

# Using min heap
import heapq
def maxOverlap_MINHEAP(intervals):
    heap = []
    intervals.sort(key=lambda interval: interval[0])
    for interval in intervals:
        if heap!=[] and heap[0] <= interval[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
    return len(heap)

intervals = [(30, 75), (0, 50), (60, 150)]
print(maxOverlap_MINHEAP(intervals))
