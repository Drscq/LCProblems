# 239 Sliding Window Maximum

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

## Examples

**Example 1:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               ---------------------
[1  3  -1] -3  5  3 6  7       3
 1 [3  -1  -3] 5  3 6  7       3
 1  3 [-1  -3  5] 3 6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3 6] 7       6
 1  3  -1  -3  5 [3 6  7]      7
```
**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```
## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Solution

### Approach: brute force

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        for (int i = 0; i <= n - k; ++i) {
            int mx = INT_MIN;
            for (int j = i; j < i + k; ++j) {
                mx = max(mx, nums[j]);
            }
            ans.push_back(mx);
        }
        return ans;
    }
};
```
### Approach: Deque

```cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        if (k == 1 || n == 0) return nums;
        if (k >= n) return { *max_element(nums.begin(), nums.end()) };

        deque<int> dq;              // store indices, values decreasing
        vector<int> ans;
        ans.reserve(n - k + 1);

        for (int i = 0; i < n; ++i) {
            // 1) pop indices that fell out of the window [i-k+1, i]
            if (!dq.empty() && dq.front() <= i - k) dq.pop_front();

            // 2) maintain decreasing order: remove smaller/equal from back
            while (!dq.empty() && nums[dq.back()] <= nums[i]) dq.pop_back();

            dq.push_back(i);

            // 3) window formed, front is the max
            if (i >= k - 1) ans.push_back(nums[dq.front()]);
        }
        return ans;
    }
};
```