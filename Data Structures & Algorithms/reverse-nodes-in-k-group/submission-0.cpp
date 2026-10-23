
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode dummy(0);
        dummy.next = head;

        ListNode* prevGroup = &dummy;

        while (true) {
            ListNode* kth = prevGroup;

            // Find the kth node
            for (int i = 0; i < k && kth != nullptr; i++) {
                kth = kth->next;
            }

            // Fewer than k nodes remain
            if (kth == nullptr) {
                break;
            }

            ListNode* nextGroup = kth->next;

            // Reverse the current group
            ListNode* prev = nextGroup;
            ListNode* curr = prevGroup->next;

            while (curr != nextGroup) {
                ListNode* temp = curr->next;
                curr->next = prev;
                prev = curr;
                curr = temp;
            }

            // Connect the reversed group
            ListNode* temp = prevGroup->next;
            prevGroup->next = kth;
            prevGroup = temp;
        }

        return dummy.next;
    }
};

