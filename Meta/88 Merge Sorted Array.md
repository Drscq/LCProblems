# 88. Merge Sorted Array

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but insttead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

## Example 1:
```python
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6].
```

## Example 2:
```python
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and []. The result of the merge is [1].
```

## Example 3:
```python
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1]. The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```
## Solution
**Intution**:
To merge two sorted arrays, we can use a two-pointer approach starting from the end of both arrays. This way, we can fill `nums1` from the back without overwriting any elements that haven't been processed yet.

```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int index2 = n - 1;
        int index1 = m - 1;
        int index_new = m + n - 1;
        while (index1>= 0 && index2>= 0) {
            if (nums1[index1] > nums2[index2]) {
                nums1[index_new--] = nums1[index1--];
            } else {
                nums1[index_new--] = nums2[index2--];
            }
        }
        // while (index1>= 0 && index_new >= 0) {
        //     nums1[index_new--] = nums1[index1--];
        // }
        while (index2>= 0 && index_new >= 0) {
            nums1[index_new--] = nums2[index2--];
        }
        
    }
};
```

### Approach: one while loop
```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int p = m + n - 1;
        while (p2 >= 0) {
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[p--] = nums1[p1--];
            } else {
                nums1[p--] = nums2[p2--];
            }
        }
    }
};
