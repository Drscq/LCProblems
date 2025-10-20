# 408 Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

- "s10n" ("s <ins>ubstitutio</ins> n")

- "sub4u4n" ("sub <ins>stitu</ins> n <ins>tion</ins>")

- "12" ("<ins>substitution</ins>")

- "su3i1u2on" ("su <ins>bst</ins> i <ins>t</ins> u <ins>ti</ins> on")

- "substitution" (no substring replaced)


The following are not valid abbreviations:

- "s55n" ("s <ins>ubsti</ins>  <ins>tuti</ins> on", the replaced substrings are adjacent)

- "s010n" (leading zeros in the number)

- "s0n" (the replaced substring is empty)


Given a string `word` and an abbreviation `abbr`, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.


## Example 1

Input: word = "internationalization", abbr = "i12iz4n"
Output: true

Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i <ins>nternation</ins> aliz <ins>atio</ins> n").


## Example 2

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e" because the substring "pp" is not adjacent to the substring "le".


## Constraints
- `1 <= word.length <= 20`
- `word` consists of lowercase English letters.
- `1 <= abbr.length <= 10`
- `abbr` consists of lowercase English letters and digits.

- All the integers in `abbr` will fit in a 32-bit integer.

# Solution

## Intution

We use two pinters:
 * `i` for the word
 * `j` for the abbreviation


 At each step:

 * if `abbr[j]` is a digit:

    - Collect the full number (multi-digit allowed)
    - Move `i` ahead by that number of characters
    - Be careful : a number starting with `0` is invalid

* If `abbr[j]` is a letter:

    - It must match `word[i]`, otherwise return `False`


```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
```

```cpp
class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int i = 0, j = 0;
        while (i < word.size() && j < abbr.size()) {
            if (isdigit(abbr[j])) {
                if (abbr[j] == '0') {
                    return false;
                }
                int num = 0;
                while (j < abbr.size() && isdigit(abbr[j])) {
                    num = num * 10 + (abbr[j] - '0');
                    j++;
                }
                i += num;
            } else {
                if (i >= word.size() || word[i] != abbr[j]) {
                    return false;
                }
                i++;
                j++;
            }
        }
        return i == word.size() && j == abbr.size();
    }
};
```

## My second try:
```python
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if (abbr[j] == '0'):
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num

                if i < len(word) and j < len(abbr) and word[i] != abbr[j]:
                    return False
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return (i == len(word) and j == len(abbr))
```

        

