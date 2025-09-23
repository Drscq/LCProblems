# 54 Spiral Matrix

Given an $m \times n$ matrix, return all elements of the matrix in spiral order.

## Examples

**Example 1:**

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```
## Constraints
- $m == matrix.length$
- $n == matrix[i].length$
- $1 <= m, n <= 10$
- $-100 <= matrix[i][j] <= 100$

## Solutions

### Approach 1: Simulation

```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> ans;
        int circles = min(m, n) / 2;
        for (int r = 0; r < circles; ++r) {
            int i = r, j = r;
            int row_num = m - 2 * r;
            int col_num = n - 2 * r;
            // single row
            if (row_num == 1) {
                for (; j < r + col_num; ++j) {
                    ans.push_back(matrix[i][j]);
                }
                continue;
            }
            // single column
            if (col_num == 1) {
                for (; i < r + row_num; ++i) {
                    ans.push_back(matrix[i][j]);
                }
                continue;
            }
            // top row
            for (; j < r + col_num - 1; ++j) {
                ans.push_back(matrix[i][j]);
            }
            // right column
            for (; i < r + row_num - 1; ++i) {
                ans.push_back(matrix[i][j]);
            }
            // bottom row
            for (; j > r; --j) {
                ans.push_back(matrix[i][j]);
            }
            // left column 
            for (; i > r; --i) {
                ans.push_back(matrix[i][j]);
            }
        }
        return ans;
    }
};
```
