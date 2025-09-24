# 67 Add Binary
Given two binary strings `a` and `b`, return their sum as a binary string.

## Examples

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```
**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```
## Constraints
- $1 <= a.length, b.length <= 10^4
- `a` and `b` consist only of `'0'` or `'1'`.
- Each string does not contain leading zeros except for the zero itself.


## Solutions

### Approach 1: Simulate Binary Addition
```c++
class Solution {
public:
    string addBinary(string a, string b) {
        string result = "";
        int carry = 0;
        int i = a.size() - 1;
        int j = b.size() - 1;
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) sum += a[i--] - '0';
            if (j >= 0) sum += b[j--] - '0';
            result += (sum % 2) + '0';
            carry = sum / 2;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```


```c++
class Solution {
public:
    string addBinary(string a, string b) {
        int m = a.size();
        int n = b.size();
        stack<int> st;
        if (m < n) {
            for (int i = 0; i < n - m; i++) {
                a = '0' + a;
            }
        }
        if (n < m) {
            for (int i = 0; i < m - n; i++) {
                b = '0' + b;
            }
        }
        int mn = max(m, n);
        int carry = 0;
        for (int i = mn - 1; i >= 0; --i) {
            if (a[i] == '1' && b[i] == '1') {
                if (carry == 0) {
                    st.push('0');
                } else {
                    st.push('1');
                }
                carry = 1;
            } else if (a[i] == '0' && b[i] == '0') {
                if (carry == 0) {
                    st.push('0');
                } else {
                    st.push('1');
                }
                carry = 0;
            } else {
                if (carry == 0) {
                    st.push('1');
                    carry = 0;
                } else {
                    st.push('0');
                    carry = 1;
                }
            }
        }
        if (carry == 1) {
            st.push('1');
        }
        string ans = "";
        while (!st.empty()) {
            ans += st.top();
            st.pop();
        }
        return ans;
    }
};
```

