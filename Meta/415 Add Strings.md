# 415 Add Strings

Given two non-negative integers, `num1` and `num2` represented as string, return the sum of `num1` and `num2` as a string.

You must solve the problem without using any built-in library for handling large integers (such as `BigInteger`) and you cannot convert the inputs to integers directly.

## Examples
**Example 1:**
```
Input: num1 = "11", num2 = "123"
Output: "134"
```
**Example 2:**
```
Input: num1 = "456", num2 = "77"
Output: "533"
```
**Example 3:**
```
Input: num1 = "0", num2 = "0"
Output: "0"
```

## Constraints
- `1 <= num1.length, num2.length <= 10^4`
- `num1` and `num2` consist of only digits.
- `num1` and `num2` do not contain any leading zeros except for the zero itself.

## Solution

### Approach: Simulate Addition
To add two numbers represented as strings, we can simulate the addition process digit by digit, starting from the least significant digit (the end of the strings). We maintain a carry for sums that exceed 9.

```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        string result;
        int carry = 0;
        int i = num1.size() - 1;
        int j = num2.size() - 1;

        while (i >= 0 || j >= 0 || carry) {
            int digit1 = (i >= 0) ? num1[i--] - '0' : 0;
            int digit2 = (j >= 0) ? num2[j--] - '0' : 0;
            int sum = digit1 + digit2 + carry;
            carry = sum / 10;
            result.push_back((sum % 10) + '0');
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```

### Complexity Analysis
- **Time Complexity:** O(max(N, M)), where N and M are the lengths of `num1` and `num2`. We traverse both strings once.
- **Space Complexity:** O(max(N, M)), for storing the result string.

### Approach: Using Built-in Functions
If allowed to use built-in functions, we can convert the strings to integers, add them, and convert the result back to a string. However, this approach is not suitable for very large numbers.
```cpp
class Solution {
public:
    string addStrings(string num1, string num2) {
        long long n1 = stoll(num1);
        long long n2 = stoll(num2);
        return to_string(n1 + n2);
    }
};
```
