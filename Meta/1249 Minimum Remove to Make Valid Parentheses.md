# 1249. Minimum Remove to Make Valid Parentheses

Given a string `s` of `(`, `)`, and lowercase English characters.

Your task is to remove the minimum number of parentheses ( `(` or `)`, in any positions) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

* It is the empty string, contains only lowercase characters, or

* It can be written as `AB` (A concatenated with B), where `A` and `B` are valid strings, or

* It can be written as `(A)`, where `A` is a valid string.

## Example 1:
```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

## Example 2:
```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

## Example 3:
```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

## Constraints:
* $1 <=$ s.length $<= 10^5$
* `s[i]` is either `(`, `)`, or a lowercase English letter.


## Algorithm:

### Approach1 : Two Passes

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_to_right_res = []
        balance = 0
        for ch in s:
            if ch == '(':
                left_to_right_res.append(ch)
                balance += 1
            elif ch == ')':
                if balance:
                    balance -= 1
                    left_to_right_res.append(ch)
            else:
               left_to_right_res.append(ch)

        right_to_left_res = []
        balance = 0
        for ch in reversed(left_to_right_res):
            if ch == ')':
                right_to_left_res.append(ch)
                balance += 1
            elif ch == '(':
                if balance:
                    balance -= 1
                    right_to_left_res.append(ch)
            else:
                right_to_left_res.append(ch)
        
        return "".join(reversed(right_to_left_res))
```