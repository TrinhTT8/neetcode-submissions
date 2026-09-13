class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers problem?

        # Left = buy
        # Right = sell

        # If left pointer is larger than right pointer, we move the left pointer to the right
        # If left pointer is smaller than the right pointer, we only move the right pointer
        # Keep going until we find the maximum profit

        l, r = 0, 1
        max = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                if curr_profit > max:
                    max = curr_profit
                
                r += 1
            else:
                l = r
                r += 1
    
        return max