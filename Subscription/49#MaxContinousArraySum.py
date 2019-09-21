'''
This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''
# This is my bullshit
def findMax(arr):
    current_max = 0
    res_max = 0
    for num in arr:
        current_max += num
        if current_max < 0:
            current_max = 0
        res_max = max(res_max, current_max)
    return res_max
print(findMax([34, -50, 42, 14, -5, 86]))
'''
We can work backwards from our desired solution by iterating over the array and looking at the maximum possible subarray that can be made ending at each index. At each index, either we can include that element in our sum or we exclude it.

We can then keep track of the maximum subarray we've seen so far in a variable max_so_far, compute the maximum subarray that includes x at each iteration, and choose whichever one is bigger.

def max_subarray_sum(arr):
'''
def Kadane(arr):
    max_so_far = max_ending_here = 0
    for num in arr:
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far
print(Kadane([34, -50, 42, 14, -5, 86]))
# This algorithm is known as Kadane's algorithm, and it runs in O(N) time and O(1) space.
