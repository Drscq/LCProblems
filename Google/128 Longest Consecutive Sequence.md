# 128 Longest Consecutive Sequence

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

## Examples
**Example 1:**
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
``` 
**Example 2:**
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3
, 4, 5, 6, 7, 8]. Therefore its length is 9.
```
## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Solution

### Approach 1: brute force 
```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        int longest_streak = 1;
        int current_streak = 1;
        for (int i = 0; i < n; ++i) {
            current_streak = 1;
            int current_num = nums[i];
            while (find(nums.begin(), nums.end(), current_num + 1) != nums.end()) {
                current_streak += 1;
                current_num += 1;
            }
            longest_streak = max(longest_streak, current_streak);
        }
        return longest_streak;
    }
};
```

### Approach 2: using sorting
```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if(n == 0) return 0;
        sort(nums.begin(), nums.end());
        int longest_streak = 1;
        int current_streak = 1;
        for (int i = 1; i < n; ++i) {
            if (nums[i] != nums[i - 1]) {
                if (nums[i] == nums[i - 1] + 1) {
                    current_streak += 1;
                } else {
                    longest_streak = max(longest_streak, current_streak);
                    current_streak = 1;
                }
            }
        }
        return max(longest_streak, current_streak);
    }
};
```