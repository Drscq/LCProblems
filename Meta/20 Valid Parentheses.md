# 20. Valid Parentheses

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.

2. Open brackets must be closed in the correct order.

3. Every close bracket has a corresponding open bracket of the same type.

## Examples

### Example 1:
```
Input: s = "()"
Output: true
```

### Example 2:
```
s = "()[]{}"
Output: true
```

### Example 3:
```
s = "(]"
Output: false
```

### Example 4:
```
s = "([])"
Output: true
```

### Example 5:
```
s = "([)]"
Output: false
```

## Constraints
- $1 \leq s.length \leq 10^4$
- `s` consists of parentheses only `'()[]{}'`.


## Solution

To determine if the input string of parentheses is valid, we can use a stack data structure. The idea is to push opening brackets onto the stack and pop them when we encounter a closing bracket. If at any point we encounter a closing bracket that does not match the top of the stack, or if the stack is empty when we encounter a closing bracket, then the string is not valid.
Here is a C++ implementation of the solution:

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else {
                if (st.empty()) return false;
                char top = st.top();
                st.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return st.empty();
    }
};
```

### Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input string `s`. We traverse the string once.
- **Space Complexity**: O(n) in the worst case, if all characters in the string are opening brackets, we will push all of them onto the stack.This solution efficiently checks for the validity of the parentheses in the input string.