'''
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
'''
'''
 It's tempting to write a solution which checks whether the left node's key is less than the current node's key and the right node's key is greater than the current node's key. However, we have to make sure that the property holds for the entire subtree, not just the children. For example, the following binary tree would be considered valid if we only checked the children:

      2
     / \
    1   3
     \
      4
      '''
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    def is_bst_helper(root, min_key, max_key):
        if root is None:
            return True
        if root.key <= min_key or root.key >= max_key:
            return False
        return is_bst_helper(root.left, min_key, root.key) and is_bst_helper(root.right, root.key, max_key)
    return is_bst_helper(root, float('-inf'), float('inf'))
