'''
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
 [t, t, f, t],
 [f, f, f, f],
 [f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''
board = [[False, False, False, False],
         [True, True, False, True],
         [False, False, False, False],
         [False, False, False, False]]

# Utility Function
def walkable(board, i, j):
    return 0<=i<len(board) and 0<=j<len(board[0]) and not board[i][j]

def get_walkable(board, i, j):
    return [(r, c) for r, c in [
        (i-1, j), (i+1, j), (i, j-1), (i, j+1)
    ] if walkable(board, r, c)]

# BFS
from collections import deque
def shortest_path_BFS(board, start, end):
    seen = set()
    q = deque([(start, 0)])
    while q:
        (thiscord, count) = q.popleft()
        seen.add(thiscord)
        if thiscord == end:
            return count
        q.extend((newcord, count+1)
            for newcord in get_walkable(board, thiscord[0], thiscord[1])
            if newcord not in seen)

print("BFS: %d"%shortest_path_BFS(board, (3, 0), (0, 0)))

# DFS
# global res

def shortest_path_DFS(board, start, end):
    res = 1000
    seen = set()
    seen.add(start)
    def DFS(board, cord, count):
        if count > res:
            return
        if cord == end:
            res = min(res, count)
            return
        for newcord in get_walkable(board, cord[0], cord[1]):
            if newcord not in seen:
                seen.add(newcord)
                DFS(board, newcord, count+1)
                seen.remove(newcord)
    DFS(board, start, 0)
    return res


shortest_path_DFS(board, (3, 0), (0, 0))
print("DFS: %d"%res)
