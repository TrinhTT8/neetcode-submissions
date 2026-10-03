"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None 

        org_curr = head
        
        # Use the hash map to store the original node and the copied node
        # So when you need to reference to the random node, you can look at the hash map to find the copied node
        nodes_dict = {}

        # First pass: Copy the node and map out the hash map
        while org_curr:
            # Create a new node for every original node
            nodes_dict[org_curr] = Node(org_curr.val)
            org_curr = org_curr.next

        # Remember: None value won't be saved in the first pass so we can save it separately
        nodes_dict[None] = None
        
        # Second pass: Connect the random and next pointers
        org_curr = head
        while org_curr:
            new_curr = nodes_dict[org_curr]
            new_curr.next = nodes_dict[org_curr.next]
            new_curr.random = nodes_dict[org_curr.random]

            org_curr = org_curr.next

        return nodes_dict[head]




