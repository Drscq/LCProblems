# 27 Remove Element

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` to be `k`, to get accepted, you need to do the following things:

* Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
* Return `k`.

## Custom Judge

The judge will test your solution with the following code:

```

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
sort(expectedNums, 0, expectedNums.length); // Sort the expected array
for (int i = 0; i < expectedNums.length; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.

## Examples

**Example 1:**
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```
**Example 2:**
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```
## Constraints
* $1 <= nums.length <= 100
* $0 <= nums[i] <= 50$
* $0 <= val <= 100$

## Solution

### Approach: Two Pointers

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            if (nums[left] == val) {
                swap(nums[left], nums[right]);
                right--;
            } else {
                left++;
            }
        }
        return left;
    }
}
```

### Complexity Analysis
* Time Complexity: $O(n)$, where $n$ is the length of `nums`. We traverse the array once.
* Space Complexity: $O(1)$. We use only a constant amount of extra space

### Approach: Fast and Slow Pointers

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slow = 0;
        for (int fast = 0; fast < nums.size() ; ++fast) {
            if (nums[fast] != val) {
                nums[slow++] = nums[fast];
            }
        }
        return slow;
    }
};
```

### Complexity Analysis
* Time Complexity: $O(n)$, where $n$ is the length of `nums`. We traverse the array once.
* Space Complexity: $O(1)$. We use only a constant amount of extra space
