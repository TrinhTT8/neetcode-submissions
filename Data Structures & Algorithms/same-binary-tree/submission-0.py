# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
       # Traverse both p and q trees
       # At each node, check if the other node has the same value
       # Edge case: empty trees, uneven trees?

        if p is None and q is None:
            return True 
        elif (p is None and q is not None) or (q is None and p is not None):
            return False
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
