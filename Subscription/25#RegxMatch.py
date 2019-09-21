'''
This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

###    . (period) which matches any single character
###    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
'''

def match_first_char(s, r):
    return s[0] == r[0] or (r[0] == '.' and len(s) > 0)

def match(s, r):
    if r == '':
        return s == ''
    if len(r)==1 or r[1] != '*':
        if match_first_char(s, r):
            return match(s[1:], r[1:])
        else:
            return False
    else:
        if match(s, r[2:]):
            return True
        i = 0
        while match_first_char(s[i:], r):
            if match(s[i+1:], r[2:]):
                return True
            i += 1

# This takes O(len(s) * len(r)) time and space, since we potentially need to iterate over each suffix substring again for each character.
print(match("chat",".*at"))

# Try do this in O(max(len(s), len(r)))

# Top down dp:
def matchTDP(s, r):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(r):
                ans = i==len(s)
            else:
                first_match = i < len(s) and r[j] in [s[i], '.']
                if j+1 < len(r) and r[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)
            memo[i, j] = ans
        return memo[i, j]
    return dp(0, 0)
# Bottom up dp top down
class Solution(object):
    def isMatch1(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
    def isMatch2(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[0][0] = True
        for i in range(1, len(pattern) + 1):
            if pattern[i-1] == '*' and dp[0][i-2] == True:
                dp[0][i] = True
        for i in range(1, len(text) + 1):
            for j in range(1, len(pattern) + 1):
                if text[i - 1] == pattern[j - 1] or pattern[j - 1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j - 1] == '*':
                    if pattern[j-2] != text[i-1] and pattern[j-2] != '.':
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]

s = Solution()
print(s.isMatch2('chat', '.*at'))
