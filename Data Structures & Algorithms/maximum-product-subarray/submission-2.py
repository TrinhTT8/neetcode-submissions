class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # The elements within the subarray have to be next to each other
        res = max(nums)
        currMax, currMin = 1, 1
        # Store a min and a max for sub array
        # For every new element, multiply by the min and max of the previous element
        # An element can multiple by itself
        # Subarray can have at least 1 element

        for i in nums:
            # Check if whether the product when multiplying
            # The maximum, minimum or just itself is the maximum
            # Need a temp here because we are changing the currMax before using it for currMin
            temp = currMax
            currMax = max(i * currMax, i * currMin, i)
            currMin = min(i * temp, i * currMin, i)

            if res < max(currMax, currMin):
                res = max(currMax, currMin)
        
        return res
