# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      # Can we look at the max height of each left and right subtrees?
      # Traverse through the tree to search for the max height of left and right
      # If the difference between the height is no more than 1 we return True

        if root is None:
            return True 
        
        l_height = self.maxHeight(root.left)
        r_height = self.maxHeight(root.right)

        if abs(l_height - r_height) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

    
      