# 42 Trapping Rain Water

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Example 1:

![alt text](/Figures/google/trappingRainWater.png)
```
Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

## Example 2:
```
Input: height = [4, 2, 0, 3, 2, 5]
Output: 9
```

## Constraints:

- $n == height.length$
- $1 <= n <= 2 * 10^4$
- $0 <= height[i] <= 10^5$


## Solution:

### Approach 1: Brute force

#### Intuition

Do as directed in question. For each element in the array, we find the maximum level of water it can trap after the rain, which is equal to the minimum of maximum height of bars on both sides minus its own height.

#### Algorithm
1. Initialize $ans = 0$.
2. Iterate the array from left to right:
    * Initialize $left\_max = 0$ and $right\_max = 0$.
    * Iterate from the current element to the beginning of array updating
        * $left\_max = max(left\_max, height[j])$.
    * Iterate from the current element to the end of array updating
        * $right\_max = max(right\_max, height[j])$.
    * Add $min(left\_max, right\_max) - height[i]$ to $ans$.
3. Return $ans$.

### Implementation

```c++
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int left_max = 0, right_max = 0;
            for (int j = i; j >=0; j--) {
                left_max = max(left_max, height[j]);
            }
            for (int j = i; j < n; j++) {
                right_max = max(right_max, height[j]);
            }
            int min_height = min(left_max, right_max);
            ans += (min_height - height[i]) > 0 ? (min_height - height[i]) : 0;
        }
        return ans;
    }
}
```
The above brute force approach has a time complexity of $O(n^2)$ and space complexity of $O(1)$.

But it will face TLE for large inputs. We can keep the same idea but precompute those maxima once (classic DP/prefix-suffix sums).
The time will be reduced to $O(n)$ and space will be $O(n)$.


### Implementation

```c++
class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0) return 0;
        int ans = 0;
        vector<int> prefix_max_height(n);
        vector<int> suffix_max_height(n);
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                prefix_max_height[i] = height[i];
            } else {
                prefix_max_height[i] = max(height[i], prefix_max_height[i - 1]);
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            if (i == n - 1) {
                suffix_max_height[i] = height[i];
            } else {
                suffix_max_height[i] = max(height[i], suffix_max_height[i + 1]);
            }
        }
        for (int i = 0; i < n; i++) {
            int min_height = min(prefix_max_height[i], suffix_max_height[i]);
            ans += (min_height - height[i]) > 0 ? (min_height - height[i]) : 0;
        }
        return ans; 
    }
};
```

**Complexity Analysis:**
- Time Complexity: O(n), where n is the number of elements in the input array height
- Space Complexity: O(n), the space used to store the prefix and suffix maximum heights.