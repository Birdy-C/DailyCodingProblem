'''
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''
# this runs in O(N) time and uses O(K) space
 def build_houses(matrix):
     n = len(matrix[0])
     thisrow = [0] * n
     for r, row in enumerate(matrix):
         newrow = [0] * n
         for c, ele in enumerate(row):
             newrow[c] = min(thisrow[i] for i in range(n) if c!=i) + ele
         thisrow = newrow
     return min(thisrow)

# we only need to keep track of three variables:
#    The lowest cost of the current row
#    The index of the lowest cost
#    The second lowest cost
def build_houses_constSpace(matrix):
    lowest_cost, lowset_inx, second_lowest_cost = 0, -1, 0
    for r, row in enumerate(matrix):
        new_lowest_cost, new_lowest_inx, new_second_lowest_cost = inf, -1, inf
        for c, ele in enumerate(row):
            prev_lowest_cost = lowest_cost if c!=lowest_inx else second_lowest_cost
            cost = prev_lowest_cost + ele
            if cost < new_lowest_cost:
                new_second_lowest_cost = new_lowest_cost
                new_lowest_cost = cost
                lowest_inx = c
            elif cost < new_second_lowest_cost:
                new_second_lowest_cost = cost
        lowest_cost = new_lowest_cost
        lowest_inx  = new_lowest_inx
        second_lowest_cost = new_second_lowest_cost
    return lowest_cost 
