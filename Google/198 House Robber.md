# 198 House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```
**Example 2:**
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```
## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Solution

### Approach 1: Dynamic Programming

#### Intuition
1. **Subproblem (state) definition**: Let $dp[i]$ be the maximum amount of money you can rob from the first `i` houses. (i.e., from indices `[0, i-1]`).

2. **Optimal substructure**: Consider the last decision when computing $dp[i]$:

    * **Skip hourse i -1**: then we can take whatever is optimal for the first `i - 1` houses, which is $dp[i - 1]$.
    * **Rob house i - 1**: then we cannot rob house `i - 2`, so we can take whatever is optimal for the first `i - 2` houses, which is $dp[i - 2]$. We also add the money in house `i - 1`, which is `nums[i - 1]`. So the total amount in this case is $dp[i - 2] + nums[i - 1]$. 
3. **Recurrence relation**: Thus, we have the recurrence relation:
   $$ dp[i] = \max(dp[i - 1], dp[i - 2] + nums[i - 1]) $$
4. **Base cases**:
    * $dp[0] = 0$ (no houses, no money)
    * $dp[1] = nums[0]$ (only one house, rob it)
5. **Final answer**: The final answer will be $dp[n]$, where `n` is the number of houses.


```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        vector<int> dp(n + 1, 0);
        dp[0] = 0;
        dp[1] = nums[0];
        for (int i = 2; i <= n; ++i) {
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1]);
        }
        return dp[n];
    }
};
```