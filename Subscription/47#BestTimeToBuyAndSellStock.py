'''
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''
def maxProfit(arr):
    current_min, max_profit = arr[0], 0
    for num in arr:
        current_min = min(current_min, num)
        max_profit = max(max_profit, num - current_min)
    return max_profit
print(maxProfit([9, 11, 8, 5, 7, 10]))

def maxProfitR(arr):
    current_max, max_profit = arr[-1], 0
    for num in reversed(arr):
        current_max = max(current_max, num)
        max_profit = max(current_max - num, max_profit)
    return max_profit
print(maxProfitR([9, 11, 8, 5, 7, 10]))
