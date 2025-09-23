# 410 Split Array Largest Sum

Given an integer array `nums` and an integer `k`, split the array into `k` non-empty continuous subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of an array.

## Examples

**Example 1:**

```
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays. The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
``` 

**Example 2:**

```
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays. The best way is to split it into [1,2,3,4] and [5], where the largest sum among the two subarrays is only 9.
```

## Constraints
- $1 <= nums.length <= 10^4$
- $0 <= nums[i] <= 10^6$
- $1 <= k <= min(50, nums.length)$

## Solution

### Overview
We have an array of $n$ non-negative integers which we must split into $m$ subarrays. The goal is to split it in such a way that the largest sum of a subarray among these $m$ subarrays is minimized.

While dividing the array, we can observe that for each integer, there are two options: either add it to the current subarray or start a new subarray with it (as long as the number of subarrays does not exceed $m$). The maximum number of possible combinations is $(n-1)$ choose $(m-1)$, because we must split the array at $m-1$ positions to obtain $m$ subarrays, and there are $n-1$ positions where the array can be split. The brute-force approach would enumerate every possible combination and select the combination with the smallest maximum sum subarray. However, given the problem constraints, the worst-case scenario will have $999$ choose $49$ combinations, which is extraordinarly large. So let us try to find a better-optimized approach.

There are two characteristics of this problem that we should take note of at this time. First, as we iterate over each element, we must decide whether to add the element to the current subarray or to start a new subarray. This decision will depend on the number of subarrays we have already made. In other words, each decision we make is affected by the previous decisions we have made. Second, the problem is asking to minimize the largest sum of the subarrays. These are two common characteristics of dynamic programming problems, and as such we will first approach this problem using dynamic programming.


Note: If you arrived at this conclusion before reading this article, then you have done well! The clues in the problem description hint that we should consider using dynamic programming to solve this problem. However, what makes this problem especially tricky is that the optimal solution does not use dynamic programming. This speaks to the importance of taking a moment to consider other possible approaches, even after arriving at the first possible solution. Take a moment to try to come up with another viable approach now, and we will discuss the optimal approach last.

### Approach 1: Top-down dynamic programming with memoization

#### Intuition
Let's start with the first subarray, which can have a range like $[0, i]$. We need to decide the value of index $i$. Once we have decided the value of $i$, we can find the sum for the first subarray $sum[0, i]$. Then the problem simplifies to finding the maximum value out of $sum[0, i]$ and the largest sum subarray for the array in the range $[i+1, n-1]$ with $m-1$ subarrays. This way we are able to divide the problem into smaller subproblems.

How do we find the optimal value of $i$? Let's try with every possible value of $i$. We can try every possible first subarray and then recursively solve the remaining array. Let us define our recurrence relation $F[currIndex, subarrayCount]$ to be the minimum largest subarray sum for the array $[currIndex, n-1]$ with $subarrayCount$ subarrays, we can write it in the following way:

$$
F[currIndex, subarrayCount] = min(max(sum[currIndex, i], F[i+1, subarrayCount-1])),
$$

For all $i$ in range $[currIndex, n-subarrayCount]$. Note that the function $F$ shown here, represents $\mathsf{getMinimumLargestSplitSum}$ in the code below.

Let's break down the expression $max(sum[currIndex, i], F[i + 1, subarrayCount - 1])$, so we understand it better.

* $F[i + 1, subarrayCount - 1]$ represents the smallest possible largest sum subarray in the range $[i + 1, n - 1]$ with $subarrayCount - 1$ subarrays.

* $sum[currIndex, i]$ represents the sum of the current subarray spanning the range of $[currIndex, i]$.

* We take the $max$ of these two values, the expression as a whole represents the largetst sum subarray in the range $[currIndex, n - 1]$ with $subarrayCount$ subarrays, where the we make the first split at index $i$.

* To find the optimal place to split the array, we calculate this for all $i$ in the range $[currIndex, n - subarrayCount]$ and take the minimum value as the result.

Also, it is worth noting a small optimization that we just did here by deciding the range for $i$ as $[currIndex, n - subarrayCount]$ instead of $[currIndex, n - 1]. This is because we need to divide the array into exactly $m$ subarrays. Hence, if $i$ goes beyond $n - subarrayCount$, we will not be able to make $m$ subarrays even if we only place a single element in each of the remaining subarrays.


If we can calculate the result for the subproblem without using the above recurrence relation (a base case) then we can simply return the result instead of making further recursive calls. In this problem, when there is only one subarray remaining, all of the numbers remaining must go in that subarray, so when $subarrayCount$ is $1$, we can simply return the sum of the numbers between $currIndex$ and $n - 1$.


This recursive approach will have repeated subproblems; this can be observed in the figure below. Notice the green nodes are repeat subproblems signifying that we have already solved these subproblems before.

![alt text](/Figures/google/Split%20Array%20Largest%20Sum/repeats.png)

To avoid spending time recalculating the results for previously seen subproblems, the first time we calculate the minimum largest sum for a certain range and number of subarrays, we will store the value in an array. Then, the next time we need to calculate the result for this same range and subarray count we can loop up the result in constant time. This technique is known as memoization and it helps us avoid recalculating repeated subproblems.

#### What each DP entry means?
Let 

* `pref[i] = nums[0] + nums[1] + ... + nums[i-1]` be the prefix sum of the first `i` elements.
* `dp[i][k]` be the minimum largest sum we can get by splitting the subarray `nums[i..n-1]` into `k` subarrays.

#### Implementation
```cpp
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int n = nums.size();
        vector<long long> pref(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            pref[i] = pref[i - 1] + nums[i - 1];
        }
        const long long INF = (1LL << 62);
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, INF));
        dp[n][0] = 0; // base case
        for (int i = 1; i <= n; ++i) dp[i][1] = pref[i]; // base case
        for (int k = 2; k <= m; ++k) {
            for (int i = k; i <= n; ++i) {
                long long best = INF;
                for (int j = k - 1; j <= i - 1; ++j) {
                    long long last = pref[i] - pref[j];
                    long long cand = max(dp[j][k - 1], last);
                    best = min(best, cand);
                    // small pruning: if last >= best, then no need to try larger j
                    if (last >= best) break;
                }
                dp[i][k] = best;
            }
        }
    }
};
```