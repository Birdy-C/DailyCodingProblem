'''
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''
# What we can do, then, is this:
    # Set up two pointers at the head of the list (let's call them fast and slow)
    # Move fast up by k
    # Move both fast and slow together until fast reaches the end of the list
    # Now slow is at the N - kth node, remove it
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

def remove_kth_element_in_list(node, k):
    slow, fast = node, node
    for _ in range(k):
        fast = fast.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    to_delete = slow.next
    slow.next = slow.next.next
    del to_delete

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
remove_kth_element_in_list(head, 3)
print(head)
