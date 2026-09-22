class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Based on the length of s1, we create a fixed window size to check for the substring in s2
        # Use two hash maps to store the need characters and have characters
        # If the two hash maps are the same, we return true else false

        # Define our window
        l, r = 0, len(s1) - 1
        need = defaultdict(int)
        have = defaultdict(int)
        
        # Populate our need hash maps
        # We do need to define the 26 letters in our hashmap because we can't entirely erase a key in the have hash map 
        for i in s1:
            need[i] += 1
        
        while r < len(s2):
            for i in range(l, r + 1):
                have[s2[i]] += 1
            if need == have:
                return True
            else:
                l += 1
                r += 1
                # Delete all the keys and values so we can restart
                have.clear()
            
        return False
            
