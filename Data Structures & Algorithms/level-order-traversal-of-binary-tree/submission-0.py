# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS problem
        # Use dequeue from collections
        # deque (append, popleft)
        
        # Store the root
        # Then pop the root to store the left and right child if not None
        # At the beginning of the while loop, the queue stores all the nodes in exactly one level
        # Using the len of the queue during that time to keep track of how many elements we need to pop
        res = []
        bfs = deque()

        if not root:
            return res

        bfs.append(root)
        while len(bfs) != 0:
            level = []
            num_nodes = len(bfs)
            while num_nodes > 0:
                root = bfs.popleft()
                level.append(root.val)

                if root.left:
                    bfs.append(root.left)
                if root.right:
                    bfs.append(root.right)
                num_nodes -= 1
            res.append(level)
        
        return res
        
        # queue: []
        # list: []

        # queue: [1]
        # list: []
        
        # queue: [2, 3]
        # list: [1]
        
        # queue: [3, 4, 5]
        # list: [1, 2]

        # queue: [4, 5, 6, 7]
        # list: [1, 2, 3]