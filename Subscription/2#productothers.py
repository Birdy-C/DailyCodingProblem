'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
def product(list, index):
    right = [1 for i in range(len(list))]
    left = [1 for i in range(len(list))]
    right[0], left[-1] = list[0], list[-1]
    for i in range(1, len(list)):
        right[i] = right[i-1] * list[i]
    for i in reversed(range(len(list)-1)):
        left[i] = left[i+1] * list[i]
    print(right)
    print(left)
    return ( right[index-1] if index > 0 else 1 ) * ( left[index+1] if index < len(list)-1 else 1)
a = [1, 2, 3, 4, 5]
print(product(a, 3))
