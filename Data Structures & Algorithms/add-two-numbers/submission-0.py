# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Read through the 2 linked lists and add each node together
        # Add the sum of the nodes to a new linked list
        # Check for a carry over and add it to the linked list

        # If there sum has a carry
        # Carry = num // 10
        # Digit = num % 10

        dummy = ListNode()
        curr = dummy

        carry = 0
        # While l1, l2 or carry not equal to None
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            # Separate the value and the carry 
            total = n1 + n2 + carry
            carry = total // 10
            value = total % 10
            curr.next = ListNode(value)

            # Update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# Time complexity = O(m + n)
# m is the length of l1 and n is the length of l2
# Space complexity = O(1) extra space due to the next linked list we created

