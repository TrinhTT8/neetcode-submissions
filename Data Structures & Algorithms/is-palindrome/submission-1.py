class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Loop through the character in the string
        # Use hash map to store the letter and 
        # convert to lower case 
        # filter out alphanumeric character

        # Use a two pointer method t(l and r)
        # The string should have the same character from start to end and vice versa

        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:
            while s[l].isalnum() == False and l < len(s)-1:
                l += 1
            while s[r].isalnum() == False and r >= 0:
                r -= 1
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True
            