# 49 Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

## Examples

**Example 1:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
1. There is no string in strs that can be rearranged to form "bat".

2. The strings "nat" and "tan" can be rearranged are anagrams as they can be rearranged to form each other.

3. The strings "ate", "eat", and "tea" can be rearranged are anagrams as they can be rearranged to form each other.
```
**Example 2:**
```
Input: strs = [""]
Output: [[""]]
```
**Example 3:**
```
Input: strs = ["a"]
Output: [["a"]]
```
## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Solution

### Approach 1: Sorting

```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;
        for (const string& str : strs) {
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            anagramMap[sortedStr].push_back(str);
        }
        
        vector<vector<string>> result;
        for (auto& entry : anagramMap) {
            result.push_back(move(entry.second));
        }
        
        return result;
    }
};
```
