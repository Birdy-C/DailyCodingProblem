'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''
def countUnival(root):
    def helper(root):
        if root == None:
            return 0, True
        rightTotal, isRightUnival = helper(root.right)
        leftTotal , isLeftUnival = helper(root.left)
        total = rightTotal + leftTotal

        if isRightUnival and isLeftUnival:
            if root.left!=None and root.left.val != root.val:
                return total, False
            if root.right!=None and root.right.val != root.val:
                return total, False
            return total+1, True
    return helper(root)[0]



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('1', Node('1', Node('1')), Node('1'))

print(countUnival(node))
