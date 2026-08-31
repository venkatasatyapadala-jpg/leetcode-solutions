/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int* nodesBetweenCriticalPoints(struct ListNode* head, int* returnSize) {
    *returnSize = 2;

    int* ans = (int*)malloc(2 * sizeof(int));

    ans[0] = -1;
    ans[1] = -1;

    struct ListNode* prev = head;
    struct ListNode* curr = head->next;

    int pos = 1;
    int first = -1;
    int last = -1;
    int minDist = 1000000;

    while (curr->next != NULL) {
        struct ListNode* next = curr->next;

        // Local maximum
        if ((curr->val > prev->val && curr->val > next->val) ||
            // Local minimum
            (curr->val < prev->val && curr->val < next->val)) {

            if (first == -1) {
                first = pos;
            } else {
                int dist = pos - last;

                if (dist < minDist)
                    minDist = dist;
            }

            last = pos;
        }

        prev = curr;
        curr = next;
        pos++;
    }

    // Less than 2 critical points
    if (first == -1 || first == last) {
        return ans;
    }

    ans[0] = minDist;
    ans[1] = last - first;

    return ans;
}