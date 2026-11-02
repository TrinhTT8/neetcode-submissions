# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # The root will always be in the list
        # If we do root.left and root.right
            # If there is no root.right, we know root.left at that level is the RSV
            # Else if there is root.right, then root.right will be the RSV
        # At eat level, we take the last node that we have collected
        # If a node has both the left child and right child, we only need to look at the right child in this case
        res = []
        if not root:
            return res

        q = deque([root])
        while q:
            num_nodes = len(q)
            print(num_nodes)
            for i in range(1, num_nodes + 1):
                node = q.popleft()
                if i == num_nodes:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return res

