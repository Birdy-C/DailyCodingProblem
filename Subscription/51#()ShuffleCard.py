'''
This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
'''
# https://www.dailycodingproblem.com/solution/51?token=50043743300c75885eb6e902465f68fcc1478982d0a1752238c2404b407fc7242832c2f9
# 1 2 3
# 1 2
# 3 2 1
# 1 3 2
# 1 2 3
# 2 1
# 3 1 2
# 2 3 1
# 2 1 3
def shuffle(arr):
    n = len(arr)
    for i in range(n - 1):
        j = randint(i, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
# or
def shuffle(arr):
    n = len(arr)
    for i in range(1, n):
        j = randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
