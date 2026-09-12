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
    * Two pointers problem again
    * Have one pointer at each linked list head
    * Traverse through one linked list

**/

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Creat a dummy node so we don't run into the problem of inserting into an empty list
        ListNode dummy(0);
        ListNode* node = &dummy;

        while (list1 && list2) {
            if(list1->val < list2->val){
                node->next = list1;
                list1 = list1->next;
            }
            else {
                node->next = list2;
                list2 = list2->next;
            }
            node = node->next;
        }

        // If either one of the list is not empty, attach the rest of them into
        // the node list

        if (list1) {
            node->next = list1;
        }
        else {
            node->next = list2;
        }

        return dummy.next;
    }
};
