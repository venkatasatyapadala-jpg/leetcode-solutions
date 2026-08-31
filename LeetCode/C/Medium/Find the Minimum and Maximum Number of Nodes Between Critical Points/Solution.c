1/**
2 * Definition for singly-linked list.
3 * struct ListNode {
4 *     int val;
5 *     struct ListNode *next;
6 * };
7 */
8
9int* nodesBetweenCriticalPoints(struct ListNode* head, int* returnSize) {
10    *returnSize = 2;
11
12    int* ans = (int*)malloc(2 * sizeof(int));
13
14    ans[0] = -1;
15    ans[1] = -1;
16
17    struct ListNode* prev = head;
18    struct ListNode* curr = head->next;
19
20    int pos = 1;
21    int first = -1;
22    int last = -1;
23    int minDist = 1000000;
24
25    while (curr->next != NULL) {
26        struct ListNode* next = curr->next;
27
28        // Local maximum
29        if ((curr->val > prev->val && curr->val > next->val) ||
30            // Local minimum
31            (curr->val < prev->val && curr->val < next->val)) {
32
33            if (first == -1) {
34                first = pos;
35            } else {
36                int dist = pos - last;
37
38                if (dist < minDist)
39                    minDist = dist;
40            }
41
42            last = pos;
43        }
44
45        prev = curr;
46        curr = next;
47        pos++;
48    }
49
50    // Less than 2 critical points
51    if (first == -1 || first == last) {
52        return ans;
53    }
54
55    ans[0] = minDist;
56    ans[1] = last - first;
57
58    return ans;
59}