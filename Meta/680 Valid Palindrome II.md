# 680. Valid Palindrome II

Given a string `s`, return `true` if the `s` can be palindrome after deleting at most one character from it.

## Example 1:

```
Input: s = "aba"
Output: true
```
## Example 2:
```
Input: s = "abca"
Output: true
```
## Example 3:
```Input: s = "abc"
Output: false
```
## Constraints:
- `1 <= s.length <= `$10^5$
- `s` consists of lowercase English letters.


# Solution

## Intuition

We use the two-pointer technique, a standard method for checking palindromes:

* Start with two pointers: `left = 0` and `right = len(s) - 1`.

* Move both inward while s[left] == s[right].

* At the first mismatch, we have two options:
  - Skip the character at `left` and check if the remaining substring is a palindrome.
  - Skip the character at `right` and check if the remaining substring is a palindrome.


If either option results in a palindrome, we return `true`. If both options fail, we return `false`.

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(sub: str, start: int, end: int) -> bool:
            while start < end:
                if sub[start] != sub[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return isPalindrome(s, start + 1, end) or isPalindrome(s, start, end - 1)
            
            start += 1
            end -= 1
        return True
```
