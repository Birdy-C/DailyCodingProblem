'''
This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''
'''
Notice that whenever we add a character, it should ideally match the one on the other side of the string. We can use the following recurrence to solve this problem:

If s is already a palindrome, then just return s -- it's already the shortest palindrome we can make
If the first character of s (let's call it a) is the same as the last, then return a + make_palindrome(s[1:-1]) + a
If the first character of s is different from the last (let's call this b), then return the minimum between:
a + make_palindrome(s[1:]) + a
b + make_palindrome(s[:-1]) + b or the lexicographically earliest one if their lengths are equal.
# So a naive recursive solution might look like this:
'''
def firstPalindrome(s):
    if len(s) <= 1: return s
    if s[0] == s[-1]:
        return s[0] + firstPalindrome(s[1:-1]) + s[-1]
    else:
        a = s[0] + firstPalindrome(s[1:]) + s[0]
        b = s[-1] + firstPalindrome(s[:-1]) + s[-1]
        if len(a) > len(b):
            return b
        elif len(a) < len(b):
            return a
        else:
            return min(a, b)
print(firstPalindrome("google"))
'''
However, this algorithm runs in O(2^N) time, since we could potentially make two recursive calls each time. We can speed up using dynamic programming, as usual. We can either memoize our results so that we don't duplicate any work, or use a table and do bottom-up programming.
'''
cache = {}
def firstPalindromeMemo(s):
    if s in cache:
        return cache[s]
    if len(s) <= 1:
        cache[s] = s
        return s
    if s[0] == s[-1]:
        cache[s] = s[0] + firstPalindrome(s[1:-1]) + s[-1]
    else:
        a = s[0] + firstPalindrome(s[1:]) + s[0]
        b = s[-1] + firstPalindrome(s[:-1]) + s[-1]
        if len(a) > len(b):
            cache[s] = b
        elif len(a) < len(b):
            cache[s] = a
        else:
            cache[s] = min(a, b)
    return cache[s]
print(firstPalindromeMemo("google"))

# Bottom up DP
def firstPalindromeDP(s):
    dp = [['' for _ in range(0, len(s)+1)] for _ in range(0, len(s)+1)]
    for i in range(len(s)):
        dp[i][1] = s[i]
    for j in range(2, len(s)+1):
        for i in range(len(s)-j+1):
            text = s[i:i+j]
            first, last = text[0], text[-1]
            if first == last:
                dp[i][j] = first + dp[i+1][j-2] + last
            else:
                a = first + dp[i+1][j-1] + first
                b = last + dp[i][j-1] + last
                if len(a) < len(b):
                    dp[i][j] = a
                elif len(a) > len(b):
                    dp[i][j] = b
                else:
                    dp[i][j] = min(a, b)
    return dp[0][-1]


print(firstPalindromeDP("google"))
