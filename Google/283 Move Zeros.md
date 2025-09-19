# 283. Move Zeroes

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

You must do this **in-place** without making a copy of the array.

## Examples

**Example 1:**

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```
**Example 2:**

```
Input: nums = [0]
Output: [0]
```

## Constraints:
- $1 <= nums.length <= 10^4$
- $-2^{31} <= nums[i] <= 2^{31} - 1$

## Implementation

### Approach 1: Two Pointers

```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int point_zero = 0;
        int point_non_zero = 0;

        while (point_zero < n && point_non_zero < n) {
            while ( point_zero < n && nums[point_zero] != 0) point_zero++;
            if (point_zero == n) break;

            point_non_zero = point_zero + 1;
            while (point_non_zero < n && nums[point_non_zero] == 0) point_non_zero++;
            if (point_non_zero == n) break;

            swap(nums[point_zero], nums[point_non_zero]);
            point_zero++;
            point_non_zero++;
        }
    }
};
```