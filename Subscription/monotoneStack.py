def _nearest(arr, i):
    for j in range(1, len(arr)):
        low = i - j
        high = i + j
        if 0 <= low and arr[low] > arr[i]:
            return low
        if high < len(arr) and arr[high] > arr[i]:
            return high

def preprocess(arr):
    cache = [None for _ in range(len(arr))]

    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            cache[j + 1] = j
        elif arr[j + 1] > arr[j]:
            cache[j] = j + 1

    for i, val in enumerate(cache):
        if val is None:
            cache[i] = _nearest(arr, i)
    print(cache)
    return cache

a = [2,1,2,1,2,1,2,1,2,1,3]
b = [1,7,2,8,3,9,4,10,5,11,6,12]
c = [1,2,3,4,3,2,1]
b = c
print('What the Result Should be')
preprocess(b)

print('What it is ->')
def nearestLarger(a):
    def update(index, last, i):
        if index[last] == -1:
            index[last] = i
        elif abs(i-last) < abs(index[last]-last):
            index[last] = i
    index = [-1 for i in range(len(a))]
    mono = []
    for i, num in enumerate(a):
        while mono!=[] and a[mono[-1]] < num:
            last = mono.pop()
            update(index, last, i)
        mono.append(i)
    mono = []
    for i, num in reversed(list(enumerate(a))):
        while mono!=[] and a[mono[-1]] < num:
            last = mono.pop()
            update(index, last, i)
        mono.append(i)
    print(index)

nearestLarger(b)
