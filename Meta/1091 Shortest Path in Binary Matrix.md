# 1091 Shortest Path in Binary Matrix

Given an $n \times n$ binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., `(0, 0)`) to the bottom-right cell (i.e., `(n - 1, n - 1) `) such that:
- All the visited cells of the path are `0`.

- All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

## Examples
**Example 1:**
```
Input: grid = [[0,1],[1,0]]
Output: 2
```
**Example 2:**
```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```
**Example 3:**
```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```
## Constraints:
- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`
## Solution

#### Approach: Breadth-First Search (BFS)
```cpp
class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] == 1 || grid[n-1][n-1] == 1) return -1;

        vector<vector<int>> directions = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1},          {0, 1},
            {1, -1},  {1, 0},  {1, 1}
        };
        queue<pair<int, int>> q;
        q.push({0, 0});
        grid[0][0] = 1; // mark as visited
        int pathLength = 1;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto [x, y] = q.front();
                q.pop();
                if (x == n - 1 && y == n - 1) return pathLength;

                for (auto& dir : directions) {
                    int newX = x + dir[0];
                    int newY = y + dir[1];
                    if (newX >= 0 && newX < n && newY >= 0 && newY < n && grid[newX][newY] == 0) {
                        q.push({newX, newY});
                        grid[newX][newY] = 1; // mark as visited
                    }
                }
            }
            pathLength++;
        }
        return -1;
    }
};
``` 
### Complexity Analysis
- **Time Complexity:** $O(n^2)$, where n is the number of rows (or columns) in the grid. In the worst case, we may need to visit all cells in the grid.
- **Space Complexity:** $O(n^2)$ in the worst case, where we may need to store all cells in the queue.
