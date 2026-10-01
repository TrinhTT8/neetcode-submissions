# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Divide the linked list in two
        # Use fast and slow pointer to determine the middle
        # Slow always half behind fast and when fast reaches the end, slow should be halfway through the linked list
        # Reverse the order of the second half of the linked list
        # Add the second half to the first half based on the given sequence

        f = s = head
        while f and f.next:
            s = s.next
            f = f.next.next

        list2 = s

        prev = None
        curr = list2

        # Reverse the linked list order
        while curr:
            temp = curr.next #8
            curr.next = prev #6 -> None
            prev = curr #6 
            curr = temp # 8
        list2 = prev
        
        list2_head = list2
        while head and list2_head.next:
            temp = head.next
            head.next = list2_head
            list2_temp = list2_head.next
            head.next.next = temp

            list2_head = list2_temp
            head = head.next.next

