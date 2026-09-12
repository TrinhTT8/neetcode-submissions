class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The start of each sequence does not have a left neighbor
        # Turn our array into a set for easier lookup

        numSet = set(nums)
        longest = 0

        # After finding out the start of the sequence, we should be able to find the rest of the elements

        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                # find the consecutive numbers by adding the length to the current number
                while (n+length) in numSet:
                    length += 1
                    print(length)
                longest = max(length, longest)

        return longest
            



