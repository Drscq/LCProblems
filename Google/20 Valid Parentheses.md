# 20. Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.

2. Open brackets must be closed in the correct order.

3. Every close bracket has a corresponding open bracket of the same type.

## Example 1:

```
Input : s = "()"
Output: true
```

## Example 2:

```
Input : s = "()[]{}"
Output: true
```

## Example 3:

```
Input : s = "(]"
Output: false
```

## Example 4:

```
Input : s = "([])"
Output: true
```

## Example 5:

```
Input : s = "([)]"
Output: false
```

## Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.


## Solution
```c++
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(char c : s) {
            if(c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else {
                if(st.empty()) return false;
                char top = st.top();
                st.pop();
                if((c == ')' && top != '(') || 
                   (c == '}' && top != '{') || 
                   (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return st.empty();
    }
}
```

### Implementation with coundting brackets with check mataching
```c++
class Solution {
public:
    bool isValid(string s) {
        int parentheses_left = 0;
        int parentheses_right = 0;
        int curly_bracket_left = 0;
        int curly_bracket_right = 0;
        int square_bracket_left = 0;
        int square_bracket_right = 0;
        vector<char> st;
        st.reserve(s.size());
        for (auto& ch : s) {
            if (ch == '(') {
                parentheses_left++;
                st.push_back(ch);
            } else if (ch == ')') {
                parentheses_right++;
                if (st.empty() || st.back() != '(') return false;
                st.pop_back();
            } else if (ch == '{') {
                curly_bracket_left++;
                st.push_back(ch);
            } else if (ch == '}') {
                curly_bracket_right++;
                if (st.empty() || st.back() != '{') return false;
                st.pop_back();
            } else if (ch == '[') {
                square_bracket_left++;
                st.push_back(ch);
            } else if (ch == ']') {
                square_bracket_right++;
                if (st.empty() || st.back() != '[') return false;
                st.pop_back();
            }
        }
        return st.empty() && parentheses_left == parentheses_right && curly_bracket_left == curly_bracket_right && square_bracket_left == square_bracket_right;
    }
};
```