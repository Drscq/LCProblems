# 129 Sum Root to Leaf Numbers

You are given the `root` of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path `1->2->3` represents the number `123`.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

## Examples

**Example 1:**

```
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path `1->2` represents the number `12`.
The root-to-leaf path `1->3` represents the number `13`.
Therefore, sum = 12 + 13 = 25.
```

**Example 2:**

```
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path `4->9->5` represesnts the number 495.
The root-to-leaf path `4->9->1` represesnts the number 491.
The root-to-leaf path `4->0` represesnts the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

## Constraints
* The number of nodes in the tree is in the range `[1, 1000]`.
* `0 <= Node.val <= 9`
* The depth of the tree will not exceed `10`.

## Solution

### Approach: Depth-First Search (DFS)
We can solve this problem using a depth-first search (DFS) approach. The idea is to traverse the tree from the root to each leaf node, constructing the number represeted by the path as we go. When we reach a leaf node, we add the constructed number to a global
sum variable.

```cpp
/**
* Definition for a binary tree node.
* struct TreeNode {
*    int val;
*    TreeNode *left;
*    TreeNode *right;
*    TreeNode() : val(0), left(nullptr), right(nullptr) {}
*    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
*    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
* };
*/
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
    int dfs(TreeNode* node, int currentNumber) {
        if (!node) return 0;
        currentNumber = currentNumber * 10 + node->val;
        if (!node->left && !node->right) {
            return currentNumber;
        }
        return dfs(node->left, currentNumber) + dfs(node->right, currentNumber);
    }
};
```