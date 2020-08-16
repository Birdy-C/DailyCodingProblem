'''
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''
def findIntersect(l1, l2):
    len1, len2 = 0, 0
    head1, head2 = l1, l2
    while l1!=None:
        len1 += 1
        l1 = l1.next
    while l2!=None:
        len2 += 1
        l2 = l2.next
    l1, l2 = head1, head2
    if len1 > len2:
        for i in range(len1-len2):
            l1 = l1.next
    else:
        for i in range(len2-len1):
            l2 = l2.next
    while l1.val != l2.val:
        l1 = l1.next
        l2 = l2.next
    return l1
