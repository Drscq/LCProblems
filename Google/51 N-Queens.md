# 51 N-Queens

The n-queens puzzle is the problem of placing n queens on an $n \times n$ chessboard such that no two queens attack each other.

Given an integer $n$, return all distinct solutions to the *n-queens puzzle*. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where `Q` and `.` both indicate a queen and an empty space, respectively.


## Examples

**Example 1:**

```
Input: $n = 4$
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

**Example 2:**

```
Input: $n = 1$
Output: [["Q"]]
```
## Constraints
- $1 \leq n \leq 9$

## Solution


### Approach 1: Backtracking

```cpp
class Solution {
public:
    vector<vector<string>> ans;
    vector<vector<string>> solveNQueens(int n) {
        vector<string> chessBoard(n, string(n, '.'));
        backTracking(chessBoard, n, 0);
        return ans;
    }

    void backTracking(vector<string>& chessBoard, int n, int rowIndex) {
        if (rowIndex == n) {
            ans.push_back(chessBoard);
            return;
        }

        for (int colIndex = 0; colIndex < n; ++colIndex) {
            if (isValid(chessBoard, rowIndex, colIndex)) {
                chessBoard[rowIndex][colIndex] = 'Q';
                backTracking(chessBoard, n, rowIndex + 1);
                chessBoard[rowIndex][colIndex] = '.';
            }
        }
    }
    bool isValid(vector<string>& chessBoard, int rowIndex, int colIndex) {
        // check column
        for (int i = 0; i < rowIndex; ++i) {
            if (chessBoard[i][colIndex] == 'Q') return false;
        }

        // check 45 degree diagonal
        for (int i = rowIndex - 1, j = colIndex - 1; i >= 0 && j >= 0; --i, --j) {
            if (chessBoard[i][j] == 'Q') return false;
        }
        // check 135 degree diagonal
        for (int i = rowIndex - 1, j = colIndex + 1; i >= 0 && j < chessBoard.size(); --i, ++j) {
            if (chessBoard[i][j] == 'Q') return false;
        }
        return true;
    }
};
```
