class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # Time complexity: O(n^2)
        # Space complexity: O(n) since we only use an additional list to store the LIS

        # Start from the end 
        # We know that at the end the subsequent is length of 1
        res = 0
        LIS = [1]*len(nums)
        # REMEMBER: Range starts from 0 not 1!
        # At the last index, the max length is 1
        # Starting at the index before the last element since we already know the LIS of the last element is always 1
        for i in range(len(nums)-1, -1, -1):
            # For each element, we go back to find the longest subsequent
            for n in range(i + 1, len(nums)):
                if nums[i] < nums[n]:
                    LIS[i] = max (LIS[i], 1+LIS[n])
        
        return max(LIS)

            