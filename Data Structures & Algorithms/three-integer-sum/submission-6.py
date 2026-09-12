class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Brute force by finding a combo at each element
        # Sort the array first
        nums.sort()
        res = []

        # Iterate through pair (index, value) of the list
        for i, a in enumerate(nums):
            # Edge case for when the list does not have any negative number
            # Then we break the loop 
            if a > 0:
                break

            # We skip the duplicate 
            if i > 0 and a == nums[i-1]:
                continue

            # At each a, we have a left and right pointer
            # Left pointer starts after i
            l = i + 1
            # Right pointer starts at the end of the list
            r = len(nums)-1

            while (l < r):
                sum3 = a + nums[l] + nums[r]

                if sum3 == 0:
                    res.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                # If the 3 sum is larger than 0 then we move the right pointer to the left
                elif sum3 > 0:
                    r -= 1
                else:
                    l += 1
            
        return res