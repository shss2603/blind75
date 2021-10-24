"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
"""
The optimum solution to this problem involves the intuition of current and overall profit and the concept of a pivot which here is the start variable
intially we see that start is 1 and on the second iteration of the loop, prices[2] = 5. The current and overall profit thus becomes 4. 
In the next iteration, 3 is observed which is greater than start(=1) but the current profit is 2 which is less than the profit. In the next iteration we find the maximum profit which is 5.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current_profit = 0
        start = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<start:
                start = prices[i]
            else:
                current_profit = prices[i]-start
                profit = max(profit,current_profit)
        return profit
