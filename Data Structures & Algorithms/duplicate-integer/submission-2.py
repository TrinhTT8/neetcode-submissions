class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        old = len(nums)
        # Convert the list into a set 
        # Remove the duplication instance
        new_set = set(nums)
        new = len(new_set)

        print(old)
        print(new)
        # If no duplicates return false
        if old == new:
            return False

        return True         