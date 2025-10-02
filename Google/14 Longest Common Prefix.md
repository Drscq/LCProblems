# 14 Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Examples:
**Example 1:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```
**Example 2:**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

## Constraints:
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

## Solution:

### Approach 1: Horizontal Scanning
1. Start with the first string as the initial prefix.
2. Compare the prefix with each string in the array, updating the prefix by removing characters from
    the end until it matches the start of the current string.
3. If at any point the prefix becomes empty, return "".
```c++
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int min_n = INT_MAX;
        for (auto& str : strs) {
            if (min_n > str.size()) min_n = str.size();
        }
        string ans = "";
        for (int i = 0; i < min_n; ++i) {
            char target = strs[0][i];
            bool isSame = true;
            for (auto& str : strs) {
                if (str[i] != target) {
                    isSame = false;
                    break;
                }
            }
            if (isSame == false) {
                break;
            } else {
                ans += target;
            }
        }
        return ans;
    }
};
```
