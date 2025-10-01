# 16 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

## Examples
**Example 1:**
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
**Example 2:**
```
Input: nums = [0,0,0], target = 1
Output: 0
```
## Constraints:

- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4

## Solution

```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        if (n == 3) return nums[0] + nums[1] + nums[2];
        int min_diff = INT_MAX;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            int start = i + 1;
            int end = n - 1;
            while (start < end) {
                int sum = nums[i] + nums[start] + nums[end];
                int d = target - sum;
                if (abs(min_diff) > abs(d)) {
                    min_diff = abs(d);
                    res = sum;
                }
                if (sum < target) {
                    start++;
                } else if (sum > target) {
                    end--;
                } else {
                    return target;
                }
            }
        }
        return res;
    }
};
```