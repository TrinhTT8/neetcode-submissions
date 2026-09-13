class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Use a dictionary to assign a key to a value
        # For every number, store its value as the key
        # If the dictionary at that key returns None then it is not a duplicate
        
        check_dup = {}

        for i in nums:
            if check_dup.get(i) == None:
                check_dup[i] = i
            else:
                return True

        return False
            