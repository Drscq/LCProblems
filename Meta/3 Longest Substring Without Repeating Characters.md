# 3. Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest substring without duplicate characters.

## Examples
### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
```
### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints:
- $0 \leq s.length \leq 10^5$
- `s` consists of English letters, digits, symbols and spaces.


## Solution

### Approach 1: Sliding Window

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> set;
        int lIdx = 0;
        int maxLength = 0;
        for (int rIdx = 0; rIdx < s.length(); rIdx++) {
            while (set.find(s[rIdx]) != set.end()) {
                set.erase(s[lIdx]);
                lIdx++;
            }
            set.insert(s[rIdx]);
            maxLength = max(maxLength, rIdx - lIdx + 1);
        }
        return maxLength;
    }
};
```