class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
    # Negative marking approach
    # Instead of comparing the values, we treat each value as an index
    # Remember that the intgers range from [1,n]
    # But the the array index starts at 0
    # To find the index: value - 1
    # Then we would make the value of the index negative
    # If we ever encounter a number that is already negative then we have found the duplicate

        for i in nums:
            idx = abs(i) - 1
            if nums[idx] < 0:
                return abs(i)
            else:
                nums[idx] = nums[idx] * -1
            
        return -1

      # Time complexity: O(n)
      # Space complexity: O(1)