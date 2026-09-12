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
            temp = curr->next;
            curr->next = head;
            head = curr;
            curr = temp;
        }
        return head;
    }
};
