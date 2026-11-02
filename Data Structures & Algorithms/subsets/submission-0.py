class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # A set will always include empty set
        # The set will have 2^n subsets since you have two decisions for each element (include or exclude)
        
        # Backtracking (recursion)
        # Base case: Return the subsets when index == len(nums); already at the last element
        # During each call, you include the element
        # Then recursively call the function with the previous state 
        # Then do not include the element
        res = []
        curr = []

        def backtrack(index):
            if index == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[index])
            backtrack(index + 1)
            curr.pop()
            backtrack(index + 1)
        
        backtrack(0)
        return res
