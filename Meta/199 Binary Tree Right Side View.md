# 199 Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Examples

**Example 1:**

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```
**Example 2:**

```
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```
**Example 3:**

```
Input: root = [1,null,3]
Output: [1,3]
```
**Example 4:**

```
Input: root = []
Output: []
```

## Constraints:
- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Solution

### Approach: Depth-First Search (DFS)

```cpp
/**
  * Definition for a binary tree node.
  * struct TreeNode {
  *    int val;
  *    TreeNode *left;
  *    TreeNode *right;
  *    TreeNode() : val(0), left(nullptr), right(nullptr) {}
  *    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  *    TreeNode(int x, TreeNode *left, TreeNode *right) : val*(x), left(left), right(right) {}
  * };
*/
class Solution {
public:
    void dfs(TreeNode* node, int depth, vector<int>& result) {
        if (!node) return;
        
        // If this is the first time we reach this depth, add the node's value
        if (depth == result.size()) {
            result.push_back(node->val);
        }
        
        // Traverse right subtree first to ensure rightmost nodes are processed first
        dfs(node->right, depth + 1, result);
        dfs(node->left, depth + 1, result);
    }
    
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        dfs(root, 0, result);
        return result;
    }
};
```

The above C++ code defines a solution to the problem of finding the right side view of a binary tree using a depth-first search (DFS) approach. The `dfs` function traverses the tree, prioritizing the right subtree to ensure that the rightmost nodes at each depth are recorded first. The `rightSideView` function initializes the result vector and starts the DFS traversal from the root node.

#### Complexity Analysis:
- **Time Complexity:** O(N), where N is the number of nodes in the binary tree. Each node is visited exactly once.
- **Space Complexity:** O(H), where H is the height of the tree, which is the space used by the recursion stack. In the worst case (a skewed tree), this can be O(N).