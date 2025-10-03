# 100 Same Tree

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Examples
**Example 1:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```
**Example 2:**
```
Input: p = [1,2], q = [1,null,2]
Output: false
```
**Example 3:**
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## Constraints:
- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Solution

### Approach 1: Recursive Comparison
```c++
/**
* Definition for a binary tree node.
* struct TreeNode {
*     int val;
*     TreeNode *left;
*     TreeNode *right;
*     TreeNode() : val(0), left(nullptr), right(nullptr) {}
*     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
*     TreeNode(int x, TreeNode *left, TreeNode *right) : val
*         (x), left(left), right(right) {}
* };
*/
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true; // Both nodes are null
        if (!p || !q) return false; // One node is null, the other is not
        if (p->val != q->val) return false; // Values are different

        // Recursively check left and right subtrees
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        else if (!p && q) {
            return false;
        } else if (p && !q) {
            return false;
        }

        bool curr_res;
        if (p->val == q->val) {
            curr_res = true;
        } else {
            curr_res = false;
        }
        bool left_res = isSameTree(p->left, q->left);
        bool right_res = isSameTree(p->right, q->right);
        return curr_res && left_res && right_res; 
    }
};
```