# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # GO through two list 
    # At each number compare them and append them to the new list
    # Whichever list has the leftovers, we attach the remaining to the new list
    # Edge case: empty list

    # With dummy node you don't need to check for empty list
    # If both are empty then dummy.next returns None either way
    
    # Define a dummy node helps to shorten the code because now you don't have to find the head node anymore
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2

        # Do not return dummy since it is not the official head
        return dummy.next
            

