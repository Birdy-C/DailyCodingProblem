'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
'''
def evaluate(root):
    if not root.left and not root.right:
        return root.val
    opleft = evaluate(root.left)
    opright = evaluate(root.right)
    if root.val == '+':
        return opleft + opright
    elif root.val == '-':
        return opleft - opright
    elif root.val == '*':
        return opleft * opright
    elif root.val == '/'
        return opleft / opright
    else:
        return float('-inf')
