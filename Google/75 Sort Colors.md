# 75 Sort Colors

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


## Examples

**Example 1:**

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
**Example 2:**

```
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Constraints
- $n == nums.length$
- $1 <= n <= 300$
- `nums[i]` is `0`, `1`, or `2`.


## Solution

### Approach 1: hash map + extra array
```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        unordered_map<int, int> hashTable;
        for (auto& num : nums) {
            if (hashTable.find(num) != hashTable.end()) {
                hashTable[num]++;
            } else {
                hashTable[num] = 1;
            }
        }
        for (int i = 0; i < hashTable[0]; ++i) {
            nums[i] = 0;
        }
        for (int i = hashTable[0]; i < hashTable[0] + hashTable[1]; ++i) {
            nums[i] = 1;
        }
        for (int i = hashTable[0] + hashTable[1]; i < nums.size(); ++i) {
            nums[i] = 2;
        }
    }
};
```

#### Complexity Analysis
- Time complexity: $O(n)$, where $n$ is the length of `nums
- Space complexity: $O(1)$, since the size of the hash table is fixed.
### Approach 2: One-pass, two pointers
```cpp
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int p0 = 0, p2 = nums.size() - 1;
        for (int i = 0; i <= p2; ) {
            if (nums[i] == 0) {
                swap(nums[i], nums[p0]);
                p0++;
                i++;
            } else if (nums[i] == 2) {
                swap(nums[i], nums[p2]);
                p2--;
            } else {
                i++;
            }
        }
    }
};
```
#### Complexity Analysis
- Time complexity: $O(n)$, where $n$ is the length of `nums
- Space complexity: $O(1)$, since we only use a constant amount of extra space.