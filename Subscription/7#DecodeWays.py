'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [0 for i in range(len(s)+1)]
        cache[len(s)] = 1
        for i in reversed(range(len(s))):
            if s[i].startswith('0'):
                cache[i] = 0
            elif i == len(s) - 1:
                cache[i] = 1
            else:
                if int(s[i:i+2]) <= 26:
                    cache[i] += cache[i+2]
                cache[i] += cache[i+1]
        return cache[0]

def num_encodings(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1: # This covers empty string
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += num_encodings(s[2:])

    total += num_encodings(s[1:])
    return total
