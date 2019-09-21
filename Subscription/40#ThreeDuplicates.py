'''
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''
# this is O(N) space
def findSingle(arr):
    s = set(arr)
    return (3*sum(s) - sum(arr))//2
print('findSingle 3 by set')
print(findSingle([13, 19, 13, 13]))
print(findSingle([6, 1, 3, 3, 3, 6, 6]))
# first consider two duplicates
# We can find the unique number in an array of two duplicates by XORing all the numbers in the array. What this does is cancel out all the bits that have an even number of 1s, leaving only the unique (odd) bits out.
def findSingle2(arr):
    res = 0
    for num in arr:
        res ^= num
    return res
print('findSingle 2 by xor:')
print(findSingle2([1,2,3,4,1,2,3]))
# Let's try to extend this technique to three duplicates. Instead of cancelling out all the bits with an even number of bits, we want to cancel those out that have a number of bits that are multiple of three.
def findSingle3(arr):
    result_arr = [0] * 32
    for num in arr:
        for i in range(32):
            bit = num>>i & 1
            result_arr[i] = (result_arr[i] + bit) % 3
    result = 0
    for i, bit in enumerate(result_arr):
        if bit:
            result += 2**i
    return result
print('findSingle 3 by bit-op:')
print(findSingle3([13, 19, 13, 13]))
print(findSingle3([6, 1, 3, 3, 3, 6, 6]))
