'''
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
'''
def search(nums, target):
    if len(nums) == 0: return -1;
    i, j = 0, len(nums)
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] == target:
            return mid
        # this is to skip the duplicates
        elif nums[mid] == nums[i] == nums[j]:
            i, j = i+1, j-1
        elif nums[mid] >= nums[i]:
            if target < nums[mid] and target >= nums[i]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if target > nums[mid] and target <= nums[j]:
                i = mid + 1
            else:
                j = mid - 1
    return -1
