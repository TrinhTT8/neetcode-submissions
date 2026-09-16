class Solution:
    def isPalindrome(self, s: str) -> bool:
    
    # So we can have two pointers at the beginning and end of the string
    # At each pointer, the letters should be the same until they reach the same index

        l = 0
        r = len(s)-1
        s = s.lower()

        while l < r:
            # Skip non-alphanumeric characters until we find one
            while s[l].isalnum() != True and l < (len(s)-1):
                l += 1
            while s[r].isalnum() != True and r >= 0:
                r -= 1

            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
            
        return True