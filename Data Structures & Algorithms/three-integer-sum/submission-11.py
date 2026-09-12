class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

         # sort the list first to skip for duplicate
        nums.sort()
        print(nums)
         # track the first number and the final two numbers can be find through two pointers
        for i, a in enumerate(nums):
            # If i is not the first number and i is the same as the previous number
            if i > 0 and a == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
                
            # Two sum to find the rest of the numbers
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # there can be multiple combinations with the same first number
                    # so we still need to move the pointer
                    # by shifting one pointer, our if-else statement will handle the other pointer
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res