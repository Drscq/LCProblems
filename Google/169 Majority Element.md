# 169 Majority Element

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Examples

**Example 1:**
```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Solution

### Approach 1: Hash Map

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> countMap;
        int majorityCount = nums.size() / 2;

        for (int num : nums) {
            countMap[num]++;
            if (countMap[num] > majorityCount) {
                return num;
            }
        }
        return -1; // This line will never be reached since the majority element always exists
    }
};
```
