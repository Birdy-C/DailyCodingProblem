'''
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
'''
def qsort(arr):
    i, j, k = 0, 0, len(arr)-1
    while j <= k:
        if arr[j] == 'G':
            j += 1
        elif arr[j] == 'B':
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    return arr

print(qsort(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
