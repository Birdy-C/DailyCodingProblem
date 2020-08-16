'''
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def longestSubstr(s, N):
    bound = (0, 0)
    seen = {}
    maxstr = ""
    for i, c in enumerate(s):
        seen[c] = i
        if len(seen) > N:
            pop_key = min(seen, key=seen.get)
            bound = (seen[pop_key]+1, bound[1]+1)
            seen.pop(pop_key)
        else:
            bound = (bound[0], bound[1]+1)
        if bound[1] - bound[0]> len(maxstr):
            maxstr = s[bound[0]:bound[1]]
    return maxstr


print(longestSubstr("abcba", 2))
