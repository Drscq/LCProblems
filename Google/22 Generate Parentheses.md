# 22 Generate Parentheses

Given $n$ pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples:

**Example 1:**

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Example 2:**

```
Input: n = 1
Output: ["()"]
```
## Constraints:
- $1 \leq n \leq 8$

## Solutions:

### Approach: Backtracking

```c++
class Solution {
public:
    vector<string> ans;
    vector<string> generateParenthesis(int n) {
        ans.clear();
        string parenthesis = "()";
        string parenthesises = "";
        for (int i = 0; i < n; ++i) {
            parenthesises += parenthesis;
        }
        sort(parenthesises.begin(), parenthesises.end());
        vector<bool> visited(2 * n, false);
        string current_ans = "";
        backtrack(parenthesises, visited, current_ans);
        return ans;
    }

    void backtrack(string& parenthesises, vector<bool>& visited, string& current_ans) {
        if (current_ans.size() == parenthesises.size()) {
            ans.push_back(current_ans);
            return;
        }
        for (int i = 0; i < parenthesises.size(); ++i) {
            if (visited[i]) continue;
            if (i > 0 && parenthesises[i] == parenthesises[i - 1] && !visited[i - 1]) continue;
            if (!isValid(current_ans + parenthesises[i])) continue;
            visited[i] = true;
            current_ans.push_back(parenthesises[i]);
            backtrack(parenthesises, visited, current_ans);
            visited[i] = false;
            current_ans.pop_back();
        }   
    }
    bool isValid(string& current_ans) {
        int balance = 0;
        for (char c : current_ans) {
            if (c == '(') balance++;
            else balance--;
            if (balance < 0) return false;
        }
        return true;
    }
};
```