# 31 Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

* For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, and `[3,2,1]`.

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

* For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.

* Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.

* While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be in place and use only constant extra memory.

## Examples
**Example 1:**

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Example 2:**

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 3:**

```
Input: nums = [1,1,5]
Output: [1,5,1]
```
## Constraints
* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 1000`
## Solution

### Approach : Find the Pivot and Swap
To find the next permutation, we can follow these steps:
1. Traverse the array from the end to find the first decreasing element. Let's call this index `i`.
2. If no such index exists, it means the array is in descending order. We reverse the array to get the smallest permutation.
3. If such an index `i` is found, traverse the array from the end again to find the first element that is greater than `nums[i]`. Let's call this index `j`.
4. Swap the elements at indices `i` and `j`.
5. Finally, reverse the subarray from `i + 1` to the end of the array to get the next permutation.
```cpp
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;

        // Step 1: Find the first decreasing element from the end
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            // Step 2: Find the first element greater than nums[i] from the end
            int j = n - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            swap(nums[i], nums[j]);
        }
        // Step 3: Reverse the subarray from i + 1 to the end
        reverse(nums.begin() + i + 1, nums.end());
    }
};
```