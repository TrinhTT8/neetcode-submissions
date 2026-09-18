class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # Copy the nums to the ans array
        ans = [None] * (len(nums)*2)
        
        for i in range(0, len(ans)):
            if i < len(nums):
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-len(nums)]
        
        return ans
