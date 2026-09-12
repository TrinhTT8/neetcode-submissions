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

 /**
    * Traverse through the linked list
    * Create an unordered map that stores they key as the index and the value as the node's actual value
    * If the last node point to another another node instead of null, we can check the value to find the index key.
*/

class Solution {
public:
    bool hasCycle(ListNode* head) {
        // Flyod's Tortoise and Hare
        ListNode* slow = head;
        ListNode* fast = head;

        // Traverse through the list if slow and fast exist
        while (fast != nullptr && fast->next != nullptr){
            // Slow moves one step at a time
            slow = slow->next;
            // Fast moves two steps at a time
            fast = fast->next->next;

            if (slow == fast){
                return true;
            }
        }
        return false;
    }
};
