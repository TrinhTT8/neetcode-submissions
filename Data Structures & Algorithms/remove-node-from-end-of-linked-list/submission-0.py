# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Use a while loop to count the length of the linked list 
        # Keep track of the node
        # To delete from the end of the list we do length - nth node

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        index = 0
        target_node = length - n

        curr = head
        prev = None
        while curr:
            if index == target_node and index == 0:
                head = curr.next
                return head
            elif index == target_node:
                prev.next = curr.next
                return head
            
            index += 1
            prev = curr
            curr = curr.next

        return head
