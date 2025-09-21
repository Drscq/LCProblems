# 5 Longest Palindromic Substring

Given a string `s`, return the longest palindromic substring in `s`.

## Examples

**Example 1:**
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```
**Example 2:**
```
Input: s = "cbbd"
Output: "bb"
```

## Constraints
- $1 <= s.length <= 1000$
- `s` consist of only digits and English letters (lower-case and/or upper-case),


## Solution

### Approach 1: Check all Substrings.

#### Intuition

We can start with a brute-force approach. We will simply check if each substring is a palindrome, and take the longest one that is.

First, let us talk about how we can check if a given string is a palindrome. This is a classic problem and we can do it using two pointers. If a string is a palindrome, the first character is equal to the last character. The second character is equal to the second last character, and so on.

We initialize two pointers: one at the start of the string and another at the end of the string. We check if the characters at the pointers are equal - if they are not, we know the string cannot be a palindrome. If they are equal, we move to the next pair of the characters by moving the pointer towards each other. We continue this until we either find  a mismatch or the pointers cross each other. If the pointers meet, then we have checked all pairs and we know the string is a palindrome.

One bonus to using this algorithm is that we frequently exit early on strings that are not palindromes. If you had a string of length $1000$ and the third character and third last character were not match, we would exit the algorithm after only $3$ comparisons.

There is another optimization we can make. Because the problem wants the longest palindrome, we can start by checking the longest substrings first and iterate toward the shorter substrings. This way, the first time we find a palindrome, we can return it immediately.

#### Complexity Analysis
- Time Complexity: $O(n^3)$, where $n$ is the length of the string `s`. There are $O(n^2)$ substrings and checking if each substring
is a palindrome takes $O(n)$ time.
- Space Complexity: $O(1)$, we only use a constant amount of extra space.

### Implementation

```c++
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        for (int len = n; len > 0; --len) {
            for (int start = 0; start < n - len + 1; ++start) {
                int end = start + len - 1;
                if (isPalindrome(s, start, end)) {
                    return s.substr(start, len);
                }
            }
        }
        return "";
    }
    bool isPalindrome(const string &s, int start, int end) {
        while (start < end) {
            if (s[start++] != s[end--]) {
                return false;
            }
        }
        return true;
    }
};
```


### Approach 2: Dynamic Programming

#### Intuition

Let's say that we knew the substring with inclusive bounds $i, j$ was a palindrome. If $s[i - 1] == s[j + 1]$, then we know the substring with inclusive bounds $i - 1, j + 1$ must also be palindrome, and this check can be done in constant time.

We can flip the direction of this log as well, if $s[i] == s[j]$ and the substring $i + 1, j - 1$ is a palindrome, then the substring $i, j$ must also be a palindrome.

We know that all substrings of length 1 are palindromes. From this, we can check if each substring of length $3$ is a palindrome using the above fact. We just need to check very $i, j$ pair where $j - i = 2$. Once we know all palindromes of length $5$, and then length $7$, and so on.

What about even length palindromes? A substring of length $2$ is a palindrome if both characters are equal. That is, $i, i + 1$ is a palindrome if $s[i] == s[i + 1]$. From this, we can use the earlier logic to find all palindromes of length $4$, then $6$, and so on.

Let's use a table `dp` with dimension of $n \times n$. `dp[i][j]` is a boolean representing if the substring with inclusive bouns $i, j$ is a palindrome. We initialize `dp[i][i] = true` for all $i$ and length $1$ substring, `dp[i][i + 1] = (s[i] == s[i + 1])` for the substrings of length $2$. Then, we can fill in the rest of the table using the above logic.

Now we need to populate the table. We iterate over all $i, j$ pairs, starting with pairs that have a difference of $2$ (length $3$ substrings), then pairs with a difference of $3$ (length $4$ substrings), and so on. For each pair, we check the condition from earlier
$$
s[i] == s[j] \text{ && } dp[i + 1][j - 1]
$$
If this is true, we set `dp[i][j] = true`. If the length of this palindrome is longer than the longest one we've seen so far, we update our answer.

Because we are starting with the shortest substrings and iterating toward the longest substrings, every time we find a new palindrome, it must be the longest one we have seen so far. We can use this fact to keep track of the answer on the fly.

#### Complexity Analysis
- Time Complexity: $O(n^2)$, where $n$ is the length of the string `s`. We fill in an $n \times n$ table, and each entry takes constant time to compute.
- Space Complexity: $O(n^2)$, the space used by the table `dp`.

### Implementation

```c++
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        string ans = s.substr(0, 1);
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }
        for (int len = 2; len <= n; len++) {
            for (int start = 0; start <= n - len; ++start) {
                int end = start + len - 1;
                if (s[start] == s[end] && (len == 2 || dp[start + 1][end - 1])) {
                    dp[start][end] = true;
                    if (len > ans.size()) {
                        ans = s.substr(start, len);
                    }
                }
            }
        }
        return ans;
    }
};
```