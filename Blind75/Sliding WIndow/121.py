class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic prog
        maxProfit = 0 
        minPriceSeen = prices[0]
        for sell in prices:
            currentProfit = sell - minPriceSeen
            if maxProfit < currentProfit:
                maxProfit = currentProfit
            if sell < minPriceSeen:
                minPriceSeen = sell
        return maxProfit


