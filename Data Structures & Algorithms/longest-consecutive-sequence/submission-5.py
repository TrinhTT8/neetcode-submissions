class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We start by finding the first number of the sequence
        # This is the number without any left neighbor
        # We don't count duplicate so let's convert this into a set

        nums2 = set(nums)
        longest = 0
        # We will use hash set to store the sequence
        for n in nums2:
            if (n-1) not in nums2:
                length = 1
                while (n + length) in nums2:
                    length += 1
            
                longest = max(length, longest)
                    
        return longest
