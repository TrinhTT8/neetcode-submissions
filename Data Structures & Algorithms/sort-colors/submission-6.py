class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket sort
        # Create 3 buckets, from 0 to 2
        # Put the corresponding color into the matching bucket
        # Concatenate all the buckets in order 
        if len(nums) <= 1:
            return nums

        buckets = [[] for _ in range(4)]

        for i in nums:
            buckets[i].append(i)
        
        index = 0
        for bucket in buckets:
            for num in bucket:
                nums[index] = num
                index += 1
