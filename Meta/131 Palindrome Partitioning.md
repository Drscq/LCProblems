# 131 Palindrome Partitioning

Given a string 's', partition 's' such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of 's'.


## Examples

### Example 1:
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

### Example 2:
```
Input: s = "a"
Output: [["a"]]
```


## Constraints:
- 1 <= s.length <= 16
's' contains only lowercase English letters.


## Solution

### Approach 0: Backtracking + isPalindrome Check
```c++
class Solution {
public:
    vector<vector<string>> ans;
    vector<string> path;

    vector<vector<string>> partition(string s) {
        backtrack(s, 0);
        return ans;
    }
    void backtrack(string& s, int start) {
        if (start == s.size()) {
            ans.push_back(path);
            return;
        }
        for (int end = start; end < s.size(); ++end) {
            if (!isPalindrome(s, start, end)) continue;
            path.push_back(s.substr(start, end - start + 1));
            backtrack(s, end + 1);
            path.pop_back();
        }
    }
    bool isPalindrome(string& s, int left, int right) {
        while (left < right) {
            if (s[left++] != s[right--]) return false;
        }
        return true;
    }
};
```

### Approach 1: Backtracking + Prefix isPalindrome Table
```c++
class Solution {
public:
    vector<vector<string>> ans;
    vector<string> path;
    vector<vector<bool>> isPalindrome;

    void buildPalindromeTable(string& s) {
        int n = s.size();
        isPalindrome.resize(n, vector<bool>(n, false));
        for (int len = 1; len <= n; ++len) {
            for (int left = 0; left + len - 1 < n; ++left) {
                int right = left + len - 1;
                if (s[left] == s[right]) {
                    if (len <= 2 || isPalindrome[left + 1][right - 1]) {
                        isPalindrome[left][right] = true;
                    }
                }
            }
        }
    }

    void backtrack(string& s, int start) {
        if (start == s.size()) {
            ans.push_back(path);
            return;
        }
        for (int end = start; end < s.size(); ++end) {
            if (!isPalindrome[start][end]) continue;
            path.push_back(s.substr(start, end - start + 1));
            backtrack(s, end + 1);
            path.pop_back();
        }
    }

    vector<vector<string>> partition(string s) {
        buildPalindromeTable(s);
        backtrack(s, 0);
        return ans;
    }
};
```