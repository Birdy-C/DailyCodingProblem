'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class


The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

def serialize(root):
    if root == None:
        return "#"
    return "{} {} {}".format(root.val, serialize(root.left), serialize(root.right))

def deserialize(str):
    nodeArr = iter(str.split())
    def helper():
        val = next(nodeArr)
        if val == '#':
            return None
        cur = Node(val)
        cur.left = helper()
        cur.right = helper()
        return cur
    return helper()


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
print(deserialize(serialize(node)).left.left.val == 'left.left')
