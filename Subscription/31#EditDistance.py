'''
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
'''
def editDis(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[mj for mj in range(0, m+1)] for ni in range(0, n+1)]
    for ni in range(0, n+1): dp[ni][0] = ni
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1
    return dp[-1][-1]
    
print(editDis("kitten", "sitting"))
