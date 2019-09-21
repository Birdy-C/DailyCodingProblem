'''
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''
def capture3pass(arr):
    if len(arr) == 0: return 0
    leftmax = arr[0]
    rightmax = arr[-1]
    maxinx = arr.index(max(arr))
    total = 0
    for num in arr[1:maxinx]:
        if leftmax > num:
            total += leftmax - num
        else:
            leftmax = num
    for num in reversed(arr[maxinx:len(arr)-1]):
        if rightmax > num:
            total += rightmax - num
        else:
            rightmax = num
    return total

def capacity(arr):
    if not arr:
        return 0

    total = 0
    max_i = arr.index(max(arr))

    left_max = arr[0]
    for num in arr[1:max_i]:
        total += left_max - num
        left_max = max(left_max, num)

    right_max = arr[-1]
    for num in arr[-2:max_i:-1]:
        total += right_max - num
        print(total)
        right_max = max(right_max, num)

    return total

print(capacity([3, 0, 1, 3, 6, 5, 4, 3]))
