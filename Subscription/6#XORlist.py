'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

A    <->    B    <->    C    <->    D

B         A ⊕ C       B ⊕ D         C
for B:  A ⊕ A ⊕ C  = C
'''

import ctypes


# This is hacky. It's a data structure for C, not python.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.both = 0


class XorLinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = [] # This is to prevent garbage collection

    def add(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

        # Without this line, Python thinks there is no way to reach nodes between
        # head and tail.
        self.__nodes.append(node)


    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                node = _get_obj(next_id)
            else:
                raise IndexError('Linked list index out of range')
        return node


def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value

# add runs in O(1) time and get runs in O(N) time.
