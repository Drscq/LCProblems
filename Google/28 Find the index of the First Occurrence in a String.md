# 28 Find the Index of the First Occurrence in a String

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Examples

**Example 1**

```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```
**Example 2**

```
Input : haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```
## Constraints
- `1 <= haystack.length, needle.length <=` $10^4$
- `haystack` and `needle` consist of only lowercase English characters.

## Solution

### Approach brute force
We can use a brute-force approach to solve this problem. The idea is to iterate through the `haystack` string and for each position, check if the substring starting from that position matches the `needle` string.

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int s_haystack = haystack.size();
        int s_needle = needle.size();
        if (s_needle == 0) return 0; // If needle is empty
        for (int i = 0; i + s_needle - 1 < s_haystack; ++i) {
            int j = 0;
            for (; j < s_needle; ++j) {
                if (haystack[i + j] != needle[j]) break;
            }
            if (j == s_needle) return i; // Found a match
        }
        return -1; // No match found
    }
};
```