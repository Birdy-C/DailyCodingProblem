'''
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''
def power_set(s):
    if not s:
        return [[]]
    result = power_set(s[1:])
    return result + [subset + [s[0]] for subset in result]
