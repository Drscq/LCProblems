# 560 Subarray Sum Equals K

Given an array of integers 'nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

**Example 1:**
```
Input: nums = [1,1,1], k = 2
Output: 2
```
**Example 2:**
```
Input: nums = [1,2,3], k = 3
Output: 2
```
## Constraints
- $1 <= nums.length <= 2 * 10^4$
- -$1000 <= nums[i] <= 1000$
- -$10^7 <= k <= 10^7$


## Solutions

### Approach 1: Brute Force
```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                int sum_val = 0;
                for (int jj = i; jj <= j; ++jj) {
                    sum_val += nums[jj];
                }
                if (sum_val == k) ans++;
            }
        }
        return ans;
    }
};
```

### Approach 2: reduce above Time Complexity to O(n^2)
```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int sum_val = 0;
            for (int j = i; j < n; ++j) {
                sum_val += nums[j];
                if (sum_val == k) ans++;
            }
        }
        return ans;
    }
};
``` 