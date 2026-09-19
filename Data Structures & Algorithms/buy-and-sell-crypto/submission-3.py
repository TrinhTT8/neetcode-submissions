class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        res = 0

        # Buy and sell cannot happen on the same day
        # Sell can only occur after buy
        while sell < len(prices):
            res = max(res, (prices[sell] - prices[buy]))

            # if the selling price is smaller than the buying price
            if prices[buy] > prices[sell]:
            # make the sell day become the buy day
            # and move the sell day to the next day
                buy = sell
                sell += 1
            else:
            # else we move sell pointer to the right to continue finding the max
                sell += 1
        
        return res
