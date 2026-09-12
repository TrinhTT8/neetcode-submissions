/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// Two pointers problem
// We need to have one pointer to keep track of the current node
// Another pointer to keep track of the new head

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Traverse through the linked list

        ListNode* curr = head;
        ListNode* temp = curr;
        head = nullptr;

        // null -> 2 -> 4 -> null

        while (curr != nullptr){
            // Hold the next node so
            // when we break the link we still have access to the next node
            temp = curr->next;
            // Link the current node to the new head node
            curr->next = head;
            // Move the new head to the current node and the current node to the temporary node that we stored
            head = curr;
            curr = temp;
        }
        return head;
    }
};
