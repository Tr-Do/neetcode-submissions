class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float('inf')
        maxP = 0
        profit = 0

        for i in prices:
            if i < minP:
                minP = i
            else:
                profit = i - minP
                if profit > maxP:
                    maxP = profit
        return maxP
