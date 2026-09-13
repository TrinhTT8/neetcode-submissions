class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointers problem
        # Assume that the list is in ascending order
        # If the current sum is larger than target, we move the right pointer to to the left
        # If the current sum is smaller than target, we move the left pointer to the right

        # Find complimentary number
        # Use a hashmap to store everything

        nums_dict = {}

        # number: index
        for i in range(len(nums)):
            nums_dict[nums[i]] = i

        # Subtract the current number from the target to find the complimentary number
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums_dict and nums_dict[comp] != i:
                return [i, nums_dict[comp]]

        
     