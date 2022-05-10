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
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == nullptr){
            return head;
        }
        ListNode* list = new ListNode;
        list->val = head->val;
        ListNode* cur = head;

        while(cur->next != nullptr){
            cur = cur->next;
            ListNode* create = new ListNode;
            create->val = cur->val;
            create->next = list;
            list = create;
        }
        return list;
        
    }
};