'''
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''
# https://www.dailycodingproblem.com/solution/63?token=276cc2b0a0b4fc30fdcc7e60e2ad836219a7da872356be1671ffe40bb24ae601e8a170fb
def check_word_right(matrix, r, c, word):
    word_len = len(word)
    row_len = len(matrix[0])
    if word_len != row_len - c:
        return False
    for c1, c2 in zip(word, (matrix[r][i] for i in range(c, row_len))):
        if c1 != c2:
            return False
    return True

def check_word_down(matrix, r, c, word):
    word_len = len(word)
    col_len = len(matrix)
    if word_len != col_len - r:
        return False
    for c1, c2 in zip(word, (matrix[i][c] for i in range(r, col_len))):
        if c1 != c2:
            return False
    return True

    return ''.join([matrix[i][c] for i in range(r, min(col_len, length))])

def word_search(matrix, word):
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if check_word_right(matrix, r, c, word):
                return True
            if check_word_down(matrix, r, c, word):
                return True
    return False
