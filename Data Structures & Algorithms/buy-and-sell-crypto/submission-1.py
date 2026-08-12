class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxProfit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxProfit = max(maxProfit, price - minprice)
        return int(maxProfit)