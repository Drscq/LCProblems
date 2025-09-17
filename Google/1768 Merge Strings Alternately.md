# 1768 Merge String Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

## Example 1:

```
Input : word1 = "abc", word2 = "pqr"
Output : "apbqcr"
Explanation: The merged string will be merged as so:
word1: a  b   c
word2:   p  q   r
merged: a p b q c r
```
## Example 2:

```
Input : word1 = "ab", word2 = "pqrs"
Output : "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
```

## Example 3:

```
Input : word1 = "abcd", word2 = "pq"
Output : "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
```
## Constraints:
- $1 <= word1.length, word2.length <= 100 $
- word1 and word2 consist of lowercase English letters.

## Solution

### one pointer with traversaling common length and concatenating the rest
```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ans = "";
        int n = min(word1.length(), word2.length());
        for (int i = 0; i < n; ++i) {
            ans += word1[i];
            ans += word2[i];
        }
        if (word1.length() > n) ans += word1.substr(n, word1.length() - n);
        if (word2.length() > n) ans += word2.substr(n, word2.length() - n);
        return ans;
    }
};
```

### one pointer with traversaling max length and checking bounds
```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ans = "";
        int n = max(word1.size(), word2.size());
        for (int i = 0; i < n; ++i) {
            if (i < word1.size()) ans += word1[i];
            if (i < word2.size()) ans += word2[i];
        }
        return ans;
    }
};
```