# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - Start at a node then explores as deep as possible before backtracking
# DFS - O(H) since we are only traveling through an edge once
# DFS uses stack (LIFO)

# We are only counting the edges here! 
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # From a node, add the left height and the right height to get the diameter
        
        # Local to the diameterOfBinaryTree function only
        diameter = 0

        def dfs(root):
            # Make diameter non local so dfs function can access and modify it
            nonlocal diameter

            # Base case when there is no root
            if not root:
                return 0
            
            # Recursively find the height of the left and right subtree here
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left+right)

            # Return the height not the diameter in this function!
            return 1 + max(left, right)

        dfs(root)
        return diameter
