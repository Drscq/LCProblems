# 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Example 1:
```python
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```
## Example 2:
```python
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```
## Example 3:
```python
Input: s = " "
Output: true
Explanation: s is an empty string after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

# Solution

## Approach 1: Compare with Reverse

### Intuition
A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., "madam" or "racecar". 
A palindrome, and its reverse, are identical to each other.
### Algorithm
We will reverse the given string and compare it with the original. If those are equivalent, its a palindrome.

Since only alphanumeric characters are considered, we will filter out all other types of characters before we apply our alogorithm.

Additionally, because we are treating letters as case-insensitive, we will convert the remaining letters to lower case. The digits will be left the same.
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_list = [c for c in s if c.isalnum()]
        lowered_list = [c.lower() for c in filtered_list]
        reversed_list = lowered_list[::-1]
        return lowered_list == reversed_list
```

```C++
class Solution {
public:
    bool isPalindrome(string s) {
        string filterred_str = "";
        for (char c : s) {
            if (isalnum(c)) {
                filterred_str += tolower(c);
            }
        }
        string reversed_str = string(filterred_str.rbegin(), filterred_str.rend());
        return filterred_str == reversed_str;
    }
}
```

```c++
class Solution {
public:
    bool isPalindrome(string s) {
        string filtered_str = "";
        for (char c : s) {
            if (isalnum(c)) {
                filtered_str += tolower(c);
            }
        }
        string reversed_str = filtered_str;
        reverse(reversed_str.begin(), reversed_str.end());
        return filtered_str == reversed_str;
    }
};
```

### Complexity Analysis
* Time complexity: $O(n)$ in length $n$ of the string.

We need to iterate through the string:
1. When we filter out non-alphanumeric characters, and convert the remaining characters to lower case.
2. When we reverse the filtered string.
3. When we compare the original and the reversed strings.

Each iteration run linear in time (since each character operation completes in constant time). Thus, the effective time complexity is linear.

* Space complexity: $O(n)$ in length $n$ of the string. We need $O(n)$ additional space to store the filtered and reversed strings.

## Approach 2: Two Pointers
### Intuition

If you take any ordinary string and concatenate its reverse to it, you will get a palindrome. For example, "abc" + "cba" = "abccba".
This leads us to an interesting insight about the converse: every palindrome half is reverse of the other half.

Simply speaking, if one were to start in the middle of a palindrome, and traverse outwards, they'd the same characters, in the exact same order, in both halves.
### Algorithm
Since the input string contains characters that we need to ignore in our palindrome check, it becomes tedious to figure out the real middle point of our palindromic input.

*Instead of going outwards from the middle, we could just go inwards towards the middle*

So if we start traversing inwards, from both ends of the input string, we can expect to see the same characters, in the same order.

The resulting algorithm is simple:
* Set two pointers, one at each end of the input string.
* If the input is palindromic, both the pointers should point to equivalent characters, at all times.
    * If this condition is not met at any point of time, we break and return early with `False`.
* We can simply ignore non-alphanumeric characters by continuing to traverse further.

* Continue traversing inwards until the pointers meet in the middle.
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start <= end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True
```

```C++
class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0, end = s.size() - 1;
        while (start <= end) {
            while (start < end && !isalnum(s[start])) {
                start++;
            }
            while (start < end && !isalnum(s[end])) {
                end--;
            }
            if (tolower(s[start]) == tolower(s[end])) {
                start++;
                end--;
            } else {
                return false;
            }
        }
        return true;
    }
};
```

### Complexity Analysis

* Time complexity: $O(n)$ in length $n$ of the string. We traverse over each character at-most once, until the two pointers meet in the middle, or when we break and return early.
* Space complexity: $O(1)$. No extra space required at all.


