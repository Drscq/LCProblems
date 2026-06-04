# 200. Number of Islands

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Examples

**Example 1:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Constraints
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Solution

### Core Insight

When `dfs` sets `grid[i][j]` to `'0'`, it permanently marks the cell as visited - no separate `visited` array is needed. This is the classic flood-fill / sinking trick.

### Code

```c++
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        int rows = grid.size(), cols = grid[0].size();
        int islands = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == '1') {
                    ++islands;
                    dfs(grid, r, c, rows, cols);
                }
            }
        }
        return islands;
    }
    // Module 1 - DFS
    void dfs(vector<vector<char>>& grid, int r, int c, int rows, int cols) {
        if (!inbounds(r, c, rows, cols) || grid[r][c] == '0') return;
        grid[r][c] = '0'; // mark visited
        dfs(grid, r + 1, c, rows, cols);
        dfs(grid, r - 1, c, rows, cols);
        dfs(grid, r, c + 1, rows, cols);
        dfs(grid, r, c - 1, rows, cols);
    }
    bool inbounds(int r, int c, int rows, int cols) {
        return r >= 0 && r < rows && c >= 0 && c < cols;
    }
};
```