# 209 Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray  whose sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

## Examples

**Example 1:**
```
Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**
```
Input: target = 4, nums = [1, 4, 4]
Output: 1
```

**Example 3:**
```
Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
Output: 0
``` 

## Constraints
- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Solution

### Sliding Window Approach

The sliding window technique is an efficient way to solve this problem. The idea is to use two pointers to create a window that can expand and contract based on the sum of the elements within the window. 

```c++
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int res = INT_MAX;
        int windowSum = 0;
        int lIdx = 0;
        for (int rIdx = 0; rIdx < nums.size(); rIdx++) {
            windowSum += nums[rIdx];
            while (windowSum >= target) {
                res = min(res, rIdx - lIdx + 1);
                windowSum -= nums[lIdx++];
            }
        }
        return res == INT_MAX ? 0 : res;
    }
};
```