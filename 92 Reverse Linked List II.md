# 92 Reverse Linked List II
Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

## Examples

**Example 1:**
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

**Example 2:**
```
Input: head = [5], left = 1, right = 1
Output: [5]
```
## Constraints
- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

## Solution
```c++
/**
* Definition for singly-linked list
**/
struct ListNode {
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x): val(x), next(nullptr) {}
    ListNode(int x, ListNode *next): val(x), next(next) {}
};
```

### Approach 1: Iterative Approach
```c++
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(!head || left == right) return head;
        ListNode* dummy = new ListNode(0, head);
        ListNode* prev = dummy;
        for(int i = 0; i < left - 1; ++i) {
            prev = prev->next;
        }
        ListNode* curr = prev->next;
        for(int i = 0; i < right - left; ++i) {
            ListNode* next = curr->next;
            curr->next = next->next;
            next->next = prev->next;
            prev->next = next;
        }
        return dummy->next;
    }
};
```

### my attemp 
```c++
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* left_end = nullptr;
        ListNode* right_start = nullptr;
        ListNode* current_node = nullptr;
        ListNode* reverse_head = nullptr;
        // find the left_end node in the linked list 
        ListNode dummy(0, head);
        left_end = &dummy;
        for (int i = 0; i < left - 1; ++i) {
            left_end = left_end->next;
        }
        // find the right_start_node in the linked list
        right_start = head;
        for (int i = 0; i < right; ++i) {
            right_start = right_start->next;
        }
        // assign the current_node
        current_node = left_end->next;
        // do the reverse logic
        reverse_head = right_start;
        while (current_node != right_start) {
            // insert the node to the reversed one
            ListNode* next = current_node->next;
            current_node->next = reverse_head;
            reverse_head = current_node;
            current_node = next;
        }

        // combine the three segments
        left_end->next = reverse_head;

        return dummy.next;

    }
};
```