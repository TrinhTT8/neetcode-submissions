# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
    # Two pointers method
    # Left and right pointer will have a distance of n in between
    # When right reaches the end of the list, left will be at the target node 
    # However, our left pointer will be placed exactly on the node we want to delete
    # So we can use a dummy node to make sure it is always placed at the node before our target node
    # This helps with the edge case of the target node being the first node as well 


        dummyNode = ListNode(0, head)
        l = dummyNode
        r = head

        while n > 0:
            r = r.next
            n -= 1

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return dummyNode.next

            

