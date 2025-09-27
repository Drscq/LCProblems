# 66 Plus One

You are given a large integer represented as an integer array 'digits`, where each `digits[i]` is the ith digit fo the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## Examples

**Example 1:**
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

**Example 2:**
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```
**Example 3:**
```
Input: digits = [0]
Output: [1]
```
## Constraints
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading 0's.

## Solution

```c++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

```c++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        vector<int> ans;
        int carry = 0;
        for (int i = 0; i < n; ++i) {
            if (i == 0) {
                if (digits[n - 1 - i] == 9) {
                    ans.push_back(0);
                    if (n - 1 - i == 0) ans.push_back(1);
                    ++carry;
                } else {
                    ans.push_back(digits[n - 1 - i] + 1);
                }
            } else if (i == n - 1) {
                if (digits[n - 1 - i] == 9 && carry == 1) {
                    ans.push_back(0);
                    ans.push_back(1);
                } else {
                    ans.push_back(digits[n - 1 - i] + carry);
                }
            } else {
                if (carry == 1 && digits[n - 1 - i] == 9) {
                    ans.push_back(0);
                } else {
                    ans.push_back(digits[n - 1 - i] + carry);
                    carry = 0;
                }
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```