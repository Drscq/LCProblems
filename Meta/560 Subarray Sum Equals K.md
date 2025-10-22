# 560 Subarray Sum Equals K
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

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
- $1 \leq nums.length \leq 2 \times 10^4$
- $-1000 \leq nums[i] \leq 1000$
- $-10^7 \leq k \leq 10^7$

## Solution

### Approach 1: brute force 

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        for (int i = 0; i < n; ++i) {
            int sum = 0;
            for (int j = i; j < n; ++j) {
                sum += nums[j];
                if (sum == k) ++count;
            }
        }
        return count;
    }
};
```

### Approach 2: Prefix Sum with Hash Map
**Intuition:**
The subarray sum `sum(i, j)` can be expressed using prefix sums as: `sum(i, j) = prefixSum[j] - prefixSum[i-1]`.
To find the number of subarrays that sum to `k`, we can rearrange this to: `prefixSum[i-1] = prefixSum[j] - k`.
This means that for each prefix sum at index `j`, we need to check how many times the value `prefixSum[j] - k` has occurred before index `j`.

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefixSumCount;
        prefixSumCount[0] = 1; // Base case: one way to have sum = 0
        int currentSum = 0;
        int count = 0;

        for (int num : nums) {
            currentSum += num;
            if (prefixSumCount.find(currentSum - k) != prefixSumCount.end()) {
                count += prefixSumCount[currentSum - k];
            }
            prefixSumCount[currentSum]++;
        }

        return count;
    }
};
```