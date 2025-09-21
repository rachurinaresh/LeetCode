class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        p =0
        for i in range(n-1):
            if prices[i+1] - prices[i] > 0:
                p+=prices[i+1] - prices[i]
        return p