# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # If the tree doesn't have a root then we return None
        if not root:
            return None

        root.left, root.right = root.right, root.left

        # Iterate through the left subtree and the right subtree
        # Invert the children of the left subtree and the right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root