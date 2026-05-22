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
The naive approach uses two passes: first mark the unmatched ')' (left to right) and then mark the unmatched '(' (right to left) and finally build the result skipping the marked characters.


```c++
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        if (s.empty()) return s;
        auto invalid = markUnmatchedClose(s);
        invalid = markUnmatchedOpen(s, invalid);
        return buildResult(s, invalid);
    }
private:
    unordered_set<int> markUnmatchedClose(const string& s) {
        unordered_set<int> invalid;
        int openCount = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                ++openCount;
            } else if (s[i] == ')') {
                if (openCount > 0) {
                    --openCount;
                } else {
                    invalid.insert(i);
                }
            }
        }
        return invalid;
    }
    unordered_set<int> markUnmatchedOpen(const string& s, const unordered_set<int>& invalid) {
        unordered_set<int> result(invalid);
        int closeCount = 0;
        for (int i = s.size() - 1; i >= 0; --i) {
            if (s[i] == ')') {
                ++closeCount;
            } else if (s[i] == '(') {
                if (closeCount > 0) {
                    --closeCount;
                } else {
                    result.insert(i);
                }
            }
        }
        return result;
    }
    string buildResult(const string& s, const unordered_set<int>& invalid) {
        string res;
        res.reserve(s.size() - invalid.size());
        for (int i = 0; i < s.size(); ++i) {
            if (invalid.count(i) == 0) {
                res.push_back(s[i]);
            }
        }
        return res;
    }
};
```