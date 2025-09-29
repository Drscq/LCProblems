# 3 Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without repeating characters.

## Examples:

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints:
- $0 <= s.length <= 5 * 10^4$
- `s` consists of English letters, digits, symbols and spaces.


## Solution:

### Approach 1: Sliding Window with HashTable
```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int start = 0;
        int ans = 0;
        unordered_map<char, int> last;
        for (int i = 0; i < n; ++i) {
            char c = s[i];
            if (last.count(c) && last[c] >= start) {
                start = last[c] + 1;
            }
            last[c] = i;
            ans = max(ans, i - start + 1);
        }
        return ans;
    }
};
```

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        if (n == 0) return 0;
        if (n == 1) return 1;
        int start = 0;
        unordered_map<char, int> last;
        int ans = 1;
        int len = 0;
        for (int end = 0; end < n; ++end) {
            char c = s[end];
            if (last.count(c) && last[c] >= start) {
                ans = max(ans, end - start);
                start = last[c] + 1;
            }
            last[c] = end;
            len = end - start + 1;
        }
        return max(ans, len);
    }
};
```
