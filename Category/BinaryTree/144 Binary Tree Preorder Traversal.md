# 144 Binary Tree Preorder Traversal

Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

## Examples

**Example 1:**

```
Input: root = [1,null,2,3]
Output: [1,2,3]
```
**Example 2:**

```
Input: root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9]
Output: [1,2,4,5,6,7,3,8,9]
```
**Example 3:**

```
Input: root = []
Output: []
```
## Constraints:
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Solution

### Approach 1: Recursive

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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        preorderTraversal(root, res);
        return res;
    }
    void preorderTraversal(TreeNode* root, vector<int>& res) {
        if (!root) return;
        res.push_back(root->val);
        preorderTraversal(root->left, res);
        preorderTraversal(root->right, res);
    }
};
```