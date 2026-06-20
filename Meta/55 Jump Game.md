# 55 Jump Game

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.


## Examples

### Example 1:

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2:

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jum length is 0, which makes it impossible to reach the last index.
```


## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Solution

### Approach: Greedy
To solve this problem, we can use a greedy approach. We will keep track of the maximum index we can reach at any point in time. We iterate through the array and update this maximum reachable index based on the current index and the jump length at that index. If at any point the current index exceeds the maximum reachable index, it means we cannot reach the end of the array.


```c++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > maxReach) {
                return false; // If current index is greater than max reachable index, we cannot proceed
            }
            maxReach = max(maxReach, i + nums[i]); // Update the maximum reachable index
        }
        return true; // If we can reach the end, return true
    }

};
```