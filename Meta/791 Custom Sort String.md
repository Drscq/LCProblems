# 791 Custom Sort String

You are given two strings `order` and `s`. All the characters of `order` are **unique** and were sorted in some custom order previously.

Permute the characters of `s` so that they match the order that `order` was sorted. More specifically, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string.

Return *any permutation of* `s` *that satisfies this property*.

## Examples
**Example 1:**
```
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
```
**Example 2:**
```
Input: order = "cbafg", s = "abcd"
Output: "cbad"
Explanation: The characters "b", "c", and "a" from order for the characters in s. The character "d" does not appear in order, so its position is flexible.

Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", and "a". "d" can be at any position since it is not in order. The ouput "bcad" is valid. Other valid outputs are "bdca", "cdba", and "cbda".
```
## Constraints:
- `1 <= order.length <= 26`
- `1 <= s.length <= 200`
- `order` and `s` consist of lowercase English letters.
- All the characters of 'order' are **unique**.

## Solution:

### Approach: Counting Sort
We can use a counting sort approach to solve this problem efficiently. The idea is to count the occurrences of each character in string `s`, and then build the result string by following the order defined in string `order`. Characters that are not present in `order` can be appended at the end in any order.
```cpp
class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> charCount;
        for (char c : s) {
            charCount[c]++;
        }
        string result;
        for (char c : order) {
            if (charCount.find(c) != charCount.end()) {
                result.append(charCount[c], c);
                charCount.erase(c);
            }
        }
        for (const auto& pair : charCount) {
            result.append(pair.second, pair.first);
        }
        return result;
    }
};
```