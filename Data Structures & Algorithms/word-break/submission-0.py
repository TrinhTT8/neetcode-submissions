class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Bottom up approach DP

        # Read from the last index of the str
        # Add an extra space to the array to store the whitespace
        dp = [False] * (len(s)+1)
        dp[len(s)] = True 

        # Iterate from the end to the start of the string
        for i in range(len(s), -1, -1):
            # We have to loop through the wordDict list too
            for w in wordDict:
                # If at the current i, the length of the str is shorter than
                # the word in wordDict then we return false
                if (i + len(w) <= len(s) and s[i : i + len(w)] == w):
                    dp[i] = dp[i] or dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]



