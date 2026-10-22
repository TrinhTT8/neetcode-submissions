# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If val is larger than root.val, we will add val to the right subtree
        # If val is smaller than root.val, we will add val to the left subtree
        # There are multiple cases:
        # Node inserted at the end of a leaf node
        # Node inserted in between other nodes, so you have to move or reconnect the tree?
        # Node is the first node of the tree

        if not root:
            root = TreeNode(val)
            return root
            
        curr = root
        while curr:
            if val < curr.val and curr.left is None:
                curr.left = TreeNode(val)
            elif val < curr.val:
                curr = curr.left
            elif val > curr.val and curr.right is None:
                curr.right = TreeNode(val)
            else:
                curr = curr.right

        return root
