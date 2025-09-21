# 206 Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Examples

**Example 1:**

![alt text](/Figures/google/ReverseLinkedList/Example1.png)

**Example 2:**
```
Input : head =[]
Output : []
```

## Constraints
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

## Solutions

### Prliminary 

#### Definition for singly-linked list
```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
```

### Approach 1 : Iterative

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }
    
};
```