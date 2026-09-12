# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS - starts at a root or start node, then go as deep as possible
# before backtracking to the visited node

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Check for base case when the tree is empty 
        if not root:
            return 0

        max_depth=0
        # DFS uses stack (FILO)
        stack=[[root,1]]    # Initialize the stack with root and the corresponding level

        while stack:
            # Pop the visited node 
            node, depth = stack.pop()

            # Push in the left child first before the right child
            if node:
                max_depth = max(depth, max_depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return max_depth



        