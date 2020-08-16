'''
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
'''
# Pancake Sorting
def pancake_sort(list):
    size = len(list)
    for i in reversed(range(size)):
        maxinx = get_maxinx(list[:i+1])
        reverse(list, 0, maxinx)
        reverse(list, 0, i)
    return list

def get_maxinx(list):
    return list.index(max(list))

def reverse(list, i, j):
    while (i<j):
        list[i], list[j] = list[j], list[i]
        i += 1
        j -= 1

a = [5,3,3]
print(pancake_sort(a))
