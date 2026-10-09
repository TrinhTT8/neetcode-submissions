# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # We can reuse the logic from the same binary tree problem?
        # But how do we know what is the root parent in the original subtree>
        # We need to iterate through the tree and find the node that matches with the root node in the subroot tree
        # Then from there we compare the nodes and values of both tree
        # Return true if both trees are the same

        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            elif (not root and subRoot) or (root and not subRoot):
                return False
            if root.val != subRoot.val:
                return False
            return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

        if not root and not subRoot:
            return False
        elif (not root and subRoot) or (root and not subRoot):
            return False

        # Here we do not move the subRoot tree
        # We only move the node in the original tree
        # We move subRoot node by node in the isSameTree function
        if isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


