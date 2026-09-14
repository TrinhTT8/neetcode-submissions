class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
    # bottom up method
    # Dynamic programming
    # we break down the problem to subproblems starting at the smallest one

        dp = [amount + 1] * (amount + 1) # Size: from 0 though amount inclusive
        
        # Amount of 0 will take 0 coin
        dp[0] = 0

        # For each amount, we loop through each coin to calculate the mininum path 
        for x in range(1, amount+1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], dp[x-c] + 1)
        
        # If dp[amount] is unreachable then the it will always stay at amount+1 value like we defined from the start
        return dp[amount] if dp[amount] <= amount else -1

