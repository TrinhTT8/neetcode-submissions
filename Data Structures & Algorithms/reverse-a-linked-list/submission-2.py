# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head -> node -> node -> tail

        # Empty linked list
        if head is None:
            return head

        # Two pointer method
        # We need to save the prev node and the next node
        # We move the current pointer to the prev node
        # Save the next node in a temp since we will break the linked
        # Move the curr node and prev node to the left by 1
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # At the end our curr will point to None and prev will be out last node
        # Prev will become head
        head = prev
        return head


        