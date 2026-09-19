class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search
        # For a sorted array that has been rotated, from the middle value, we expect
        # the values to the left to be greater than the values to the right

        l, r = 0, len(nums) - 1
        res = nums[0]

        while r >= l:
            m = (r+l)//2
            res = min(res, nums[m])
            # If the mid larger than the right most number, we search right
            # Since the right side is the unsorted side
            if nums[m] >= nums[r]:
                l = m + 1      # Jump left by 1 because we already know that m is larger than the right most number
            # Else we search left
            else:
                r = m

        return res