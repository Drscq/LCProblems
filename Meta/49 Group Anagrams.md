# 49 Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Examples

### Example 1:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" can be anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
```

### Example 2:
```
Input: strs = [""]
Output: [[""]]
```
### Example 3:
```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints:
- $1 \leq \text{strs.length} \leq 10^4$
- $0 \leq \text{strs[i].length} \leq 100$  
- `strs[i]` consists of lowercase English letters.

## Solution

### Approach 1: Sorting + Hash Map
```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> mp;
        for (auto str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            mp[key].push_back(str);
        }
        for (auto it : mp) {
            res.push_back(it.second);
        }
        return res;
    }
};
```

### Approach 2 : Counting + Hash Map
```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> mp;
        for (auto str : strs) {
            vector<int> count(26, 0);
            for (auto c : str) {
                count[c - 'a']++;
            }
            string key = "";
            for (int i = 0; i < 26; i++) {
                key += to_string(count[i]) + "#";
            }
            mp[key].push_back(str);
        }
        for (auto it : mp) {
            res.push_back(it.second);
        }
        return res;
    }
};
```