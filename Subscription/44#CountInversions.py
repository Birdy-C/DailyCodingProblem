'''
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
'''
'''
We can use the following recursive, divide-and-conquer algorithm to count the number of inversions in O(N log N) time.
'''
    # First, let's separate our input array into two halves A and B
    # Count the number of inversions in each list recursively
    # Count the inversions between A and B
    # Return the sum of all three counts
'''
If we are able to count all the inversions between A and B in linear time, then according to the master theorem for divide-and-conquer recurrences), our algorithm will run in O(N log N) time, since we have the same recurrence relationship as merge sort.

How can we count the inversions between A and B in linear time? If we expand our count_inversions function to also sort the array as well, we can use a similar technique to merge sort to merge and also count the inversions between A and B. To be specific, assuming A and B are sorted, we can construct a helper function that does the following:

    ``` Scan A and B from left to right, with two pointers i and j
    ``` Compare A[i] and B[j]
            `` If A[i] is smaller than B[j], then A[i] is not inverted with anything from B, since it's expected that everything in A would be smaller than everything in B if A + B was sorted.
            `` If A[i] is greater than B[j], then B[j] is inverted with everything from A[i:], since A is sorted. Increment our counter by the number of elements in A[i:].
    ``` Append the smaller element between A[i] and B[j] to our sorted list
    ``` Return the sorted list
'''
def count_inversions(arr):
    count, _ = count_inversions_helper(arr)
    return count

def count_inversions_helper(arr):
    size = len(arr)
    if size <= 1: return 0, arr
    leftArr = arr[:size//2]
    rightArr = arr[size//2:]
    left_count, left_sorted = count_inversions_helper(leftArr)
    right_count, right_sorted = count_inversions_helper(rightArr)
    merge_count, all_sorted = merge(left_sorted, right_sorted)
    return left_count + right_count + merge_count, all_sorted

def merge(A, B):
    i, j, count = 0, 0, 0
    sorted = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            sorted.append(A[i])
            i += 1
        else:
            count += len(A[i:])
            sorted.append(B[j])
            j += 1
    sorted.extend(A[i:])
    sorted.extend(B[j:])
    return count, sorted


print(count_inversions([5, 4, 3, 2, 1]))
