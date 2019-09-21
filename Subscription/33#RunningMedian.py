'''
This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
'''
import heapq

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self,x): heapq.heappush(self.h,x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self,i): return self.h[i].val

class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)

def runningMedian(lis):
    min_heap = MinHeap()
    max_heap = MaxHeap()
    median = 0
    for num in lis:
        if len(min_heap)==0 and len(max_heap)==0:
            max_heap.heappush(num)
            median = num
        else:
            if num < median:
                max_heap.heappush(num)
                if len(max_heap) > len(min_heap)+1:
                    min_heap.heappush(max_heap.heappop())
            else:
                min_heap.heappush(num)
                if len(max_heap)+1 < len(min_heap):
                    max_heap.heappush(min_heap.heappop())
        if len(max_heap) > len(min_heap):
            median = max_heap[0]
        elif len(max_heap) < len(min_heap):
            median = min_heap[0]
        else:
            median = (max_heap[0]+min_heap[0])/2
        # print([max_heap.__getitem__(i) for i in range(0, len(max_heap))])
        print("After insert {} we have median {}".format(num, median))

runningMedian([2, 1, 5, 7, 2, 0, 5])
