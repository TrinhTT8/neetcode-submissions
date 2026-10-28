class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # We can do bubble sort but that takes O(n^2)
        # Bubble sort algorithm: Since the order is from least to greatest, we can compare the two values next to each other and swap them if the left value is greater than the right value.
        if len(nums) == 1:
            return nums

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        
        return nums
