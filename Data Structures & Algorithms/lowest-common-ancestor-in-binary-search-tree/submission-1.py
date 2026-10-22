# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If q and p are smaller than root.val, then we search the left subtree
        # If q and p are bigger than root.val, then we search the right subtree
        # If q an p are not in the same subtree, then there is a split; hence, the current root is the LCA

        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
