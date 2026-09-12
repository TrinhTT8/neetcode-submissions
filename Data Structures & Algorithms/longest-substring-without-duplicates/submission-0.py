# sliding window method
# Use set data structure
# set does not allow duplicate elements
# have two pointers 
# move the right pointer, the left pointer will be moved once a duplicate is found
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        left = 0
        sub_char = set()

        for r in range(len(s)):
            while s[r] in sub_char:
                sub_char.remove(s[left])
                left += 1

            sub_char.add(s[r])
            count = max(count, r - left + 1)
        return count

            