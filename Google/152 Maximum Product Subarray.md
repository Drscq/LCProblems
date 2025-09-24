# 152 Maximum Product Subarray

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

## Examples 

**Example 1:**
```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
**Example 2:**
```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
## Constraints
- $1 \leq \mathsf{nums.length} \leq 2 * 10^4$
- $-10 \leq \mathsf{nums[i]} \leq 10$
- The product of any prefix or suffix of `nums` is guaranteed to fit in a a 32-bit integer.

## Solution

### Approach 1: Brute Force
```c++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int maxProduct = INT_MIN;
        for (int i = 0; i < n; ++i) {
            int product = 1;
            for (int j = i; j < n; ++j) {
                product *= nums[j];
                maxProduct = max(maxProduct, product);
            }
        }
        return maxProduct;
    }
};
```

### Approach 2: Dynamic Programming
```c++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int max_product = nums[0];
        int curr_max = nums[0];
        int curr_min = nums[0];
        for (int i = 1; i < n; ++i) {
            if (nums[i] < 0) {
                swap(curr_max, curr_min);
            }
            curr_max = max(nums[i], curr_max * nums[i]);
            curr_min = min(nums[i], curr_min * nums[i]);
            max_product = max(max_product, curr_max);
        }
        return max_product;
    }
};
```
### Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array `nums`. We traverse the array once.
- **Space Complexity**: O(1). We use a constant amount of space for variables.