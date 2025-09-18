# 11. Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.


## Example 1:

```
Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is $7 * 7 = 49$.
``` 
## Example 2:

```
Input: height = [1, 1]
Output: 1
```

## Constraints:
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Solution;

### Approach 1: Brute Force
In this case, we will simply consider the area for every possible pair of lines and find out the maximum area out of those.
```
Note: Brute Force approach are often included because they are intuitive starting points when solving a problem. Howevery, they are often expected to receive Time Limit Exceeded (TLE) errors on larger test cases, since they would not be accepted in an interview setting.
```
```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int ans = INT_MIN;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int area = min(height[i], height[j]) * (j - i);
                ans = max(ans, area);
            }
        }
        return ans;
    }
}
```
#### Complexity Analysis
- Time complexity: $O(N^2)$, where N is the number of lines. We are using two nested loops to consider every possible pair of lines.
- Space complexity: $O(1)$, as we are using only a constant amount of extra space.

### Approach 2: Two Pointer

The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line. Further, the farther the lines, the more will be the area obtained.

We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines. Further, we maintain a variable maxArea to stre the maximum area obtained till now. At every step, we find out the area formed between them, update maxArea, and move the pointer pointing to the shoter line twowards the other  end by one step.

```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int left = 0; 
        int right = n - 1;
        int maxArea = INT_MIN;
        while (left < right) {
            int curArea = (right - left) * min(height[left], height[right]);
            maxArea = max(maxArea, curArea);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
};
```
