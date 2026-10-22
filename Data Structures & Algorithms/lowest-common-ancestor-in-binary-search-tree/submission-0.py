# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If p and q are less than the root, we search the left subtree
        # If p and q are larger than the root, we search the right subtree
        # If p and q are not in the same subtree, there is a split, so the root is the LCA since no other root down the tree can be the ancestor
        # If p or q equals root.val, then that's the LCA
    
        while root:     
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root

        return root