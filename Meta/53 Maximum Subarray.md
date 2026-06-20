# 53 Maximum Subarray

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

## Examples

### Example 1:

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
```

### Example 2:

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum = 1.
```

### Example 3:

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.
```

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

**Follow up:** If you have figured out the $O(n)$ solution, try coding another solution using the divide and conquer approach, which is more subtle.
## Solution

### Approach: Dynamic Programming (two dimensional)
To solve this problem, we can use a dynamic programming approach. We will create a two-dimensional array `dp` where `dp[i][j]` represents the maximum sum of the subarray that starts at index `i` and ends at index `j`. We will iterate through the array and fill in the `dp` array based on the following recurrence relation:
```
dp[i][j] = max(dp[i][j-1] + nums[j], nums[j])
```
The maximum sum of the subarray will be the maximum value in the `dp` array.

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        int maxSum = nums[0];

        for (int i = 0; i < n; ++i) {
            dp[i][i] = nums[i]; // Base case: subarray of length 1
            maxSum = max(maxSum, dp[i][i]);
            for (int j = i + 1; j < n; ++j) {
                dp[i][j] = max(dp[i][j - 1] + nums[j], nums[j]);
                maxSum = max(maxSum, dp[i][j]);
            }
        }

        return maxSum;
    }
};
```

### Approach: Dynamic Programming (Kadane's Algorithm)
To solve this problem, we can use a dynamic programming approach known as Kadane's Algorithm. The idea is to iterate through the array while keeping track of the maximum sum of a subarray that ends at the current index. We also maintain a global maximum sum that keeps track of the largest sum found so far. If the current sum becomes negative, we reset it to zero, as starting a new subarray from the next index would yield a larger sum. 

```c++
class Solution  {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int currentSum = 0;

        for (int num : nums) {
            currentSum += num;
            maxSum = max(maxSum, currentSum);
            if (currentSum < 0) {
                currentSum = 0; // Reset current sum if it becomes negative
            }
        }
        return maxSum;
    }
};
```

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentSum = 0;
        int maxSum = nums[0];
        for (int num : nums) {
            currentSum = max(num, currentSum + num);
            maxSum = max(maxSum, currentSum);
        }
        return maxSum;
    }
};
```