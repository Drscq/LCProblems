# 9. Palindrome Number

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

## Example 1:
```
Input : x = 121
Output : true
Explanation : 121 reads as 121 from left to right and from right to left.
```

## Example 2:
```
Input : x = -121
Output : false
Explanation : From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
``` 

## Constraints:
- $-2^{31} <= x <= 2^{31} - 1$


## Solution:

```c++
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) return false;
        vector<int> digits = split(x);
        int start = 0, end = digits.size() - 1;
        while (start < end) {
            if (digits[start] != digits[end]) return false;
            start++;
            end--;
        }
        return true;
    }
    vector<int> split(int x) {
        vector<int> digits;
        while (x) {
            digits.push_back(x % 10);
            x /= 10;
        }
        return digits; 
    }
};
```
