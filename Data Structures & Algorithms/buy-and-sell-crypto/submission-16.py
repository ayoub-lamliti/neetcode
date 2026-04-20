class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n_min = prices[0]
        profit = 0
        for price in prices:
            if price < n_min:
                n_min = price
            t = price - n_min
            if t > profit:
                profit = t            
        return profit