# 189 Rotate Array
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
``` 

**Example 2:**
```
Input: nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
Explanation:
rotate 1 steps to the right: [99, -1, -100, 3]
rotate 2 steps to the right: [3, 99, -1, -100]
```
## Constraints
- $1 <= nums.length <= 10^5$
- $-2^{31} <= nums[i] <= 2^{31} - 1$
- $0 <= k <= 10^5$


## Solution

### Approach 1: Using Extra Array
```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n; // in case k is greater than n
        vector<int> temp(n);
        for(int i = 0; i < n; i++) {
            temp[(i + k) % n] = nums[i];
        }
        nums = temp;
    }
};
```
### Complexity Analysis
- Time Complexity: O(n), where n is the number of elements in the array. We traverse the array once.
- Space Complexity: O(n) for the temporary array used to store the rotated elements.

### Approach 2: brute force
```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        for (int i = 0; i < k; ++i) {
            int previous = nums[n - 1];
            for (int j = 0; j < n; ++j) {
                int temp = nums[j];
                nums[j] = previous;
                previous = temp;
            }
        }
    }
};
```
### Complexity Analysis
- Time Complexity: O(n * k), where n is the number of elements in the array. We perform k rotations, and each rotation takes O(n) time.
- Space Complexity: O(1) as we are using only a constant amount of extra space.