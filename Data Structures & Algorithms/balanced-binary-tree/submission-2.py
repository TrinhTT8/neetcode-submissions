# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Traverse down the tree
        # Start at the root, we use a helper function to get the max height
        # of the left subtree and the right subtree
        # Then we calculate the different of the two heights
        # If it is greater than 0, we return False

        # Always remember the case of empty root
        if not root:
            return True

        # Define another helper function to return the max height
        # Compare the right tree and left tree
        # If the difference is greater than 1 return -1
        # Else return the max height for the parents to cross check?
        def maxHeight(root):
            if not root:
                return 0

            l_height = maxHeight(root.left)
            if l_height == -1:
                return -1

            r_height = maxHeight(root.right)
            if r_height == -1:
                return -1
            
            if abs(l_height - r_height) > 1:
                return -1

            # Else we return the max height to the root
            return 1 + max(l_height, r_height)
        
        if maxHeight(root) == -1:
            return False
        
        return True
        



