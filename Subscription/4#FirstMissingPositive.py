'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def firstMissingPos(list):
    for i in range(len(list)):
        while 1<= list[i] <= len(list) and list[i] != i+1:
            v = list[i]
            list[i], list[v-1] = list[v-1], list[i]
            if list[i] == list[list[i]-1]:
                break
    print(list)
    for idx, num in enumerate(list):
        if num != idx + 1:
            return idx + 1
    return len(list)+1

a = [3,4,-1,1]
print(firstMissingPos(a))
