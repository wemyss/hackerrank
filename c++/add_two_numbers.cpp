/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
        int digit = sum % 10;
        int carry = sum / 10;
        const auto l3 = new ListNode(digit);
        auto curr = l3;

        l1 = l1 ? l1->next : l1;
        l2 = l2 ? l2->next : l2;

        while(l1 || l2 || carry) {

            sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            digit = sum % 10;

            curr->next = new ListNode(digit);
            curr = curr->next;
            carry = sum / 10;

            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }

        return l3;
    }
};
