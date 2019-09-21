'''
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
'''

# We can do this recursively and cleverly, using Python's default argument feature. Basically, we call reverse on the node's next, but not before cleaning up some pointers first:

def reverse(head, prev=None):
    if not head:
        return prev
    tmp = head.next
    head.next = prev
    return reverse(tmp, head)

# Iteratively
def reverse(head):
    prev, current = None, head
    while current is not None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev
