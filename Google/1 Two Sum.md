# 1 Two Sum
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they added up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
``` 

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
## Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Solution

### Approach 1: Brute Force
```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> res;
        // find all possible combination of two values with different index in nums
        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    res.push_back(i);
                    res.push_back(j);
                    return res;
                }
            }
        }
        return res;
    }
};
```
**Complexity Analysis:**
- Time complexity: $O(n^2)$, where n is the number of elements in `nums`. We traverse the list containing n elements twice. For each element, we try to find its complement by looping through the rest of the list which takes O(n) time.
- Space complexity: $O(1)$. We only used a constant amount of extra space.

### Approach 2: One-pass Hash Table
```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> num_map; // value -> index
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            int complement = target - nums[i];
            if (num_map.find(complement) != num_map.end()) {
                res.push_back(num_map[complement]);
                res.push_back(i);
                return res;
            }
            num_map[nums[i]] = i;
        }
        return res;
    }
};
```
**Complexity Analysis:**
- Time complexity: $O(n)$, where n is the number of elements in `nums
`. We traverse the list containing n elements only once. Each look up in the table costs only O(1) time.
- Space complexity: $O(n)$, where n is the number of elements in `nums
`. The extra space required depends on the number of items stored in the hash table, which stores at most n elements.