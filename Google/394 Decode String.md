# 394 Decode String

Given an encoded string, return its decoded string.

The encoding rule is `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed $10^5$.

## Examples

**Example 1:**

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

**Example 2:**

```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

**Example 3:**

```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Constraints
- $1 <= s.length <= 30$
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be a valid input.

## Solution

### Approach 1: Stack

```c++
class Solution {
public:
    string decodeString(string s) {
        int n = s.size();
        stack<int> st;
        for (auto ch : s) {
            if (!st.empty() && ch == ']') {
                stack<char> st_sub_str;
                auto ele = st.top();
                st.pop();
                while (ele != '[') {
                    st_sub_str.push(ele);
                    ele = st.top();
                    st.pop();
                }
                int val = 0, base = 1;
                while (!st.empty() && isdigit(st.top())) {
                    val = (st.top() - '0') * base + val;
                    base *= 10;
                    st.pop();
                }
                string sub_str = "";
                while (!st_sub_str.empty()) {
                    sub_str += st_sub_str.top();
                    st_sub_str.pop();
                }
                for (int i = 0; i < val; i++) {
                    for (auto c : sub_str) {
                        st.push(c);
                    }
                }
            } else {
                st.push(ch);
            }
        }
        string res = "";
        stack<char> st_res;
        while (!st.empty()) {
            st_res.push(st.top());
            st.pop();
        }
        while (!st_res.empty()) {
            res += st_res.top();
            st_res.pop();
        }
        return res;
    }
};
```
