class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        best = 0

        for price in prices[1:]:
            if price < minPrice:
                minPrice = price
            current = price - minPrice
            best = max(best, current)

        return best