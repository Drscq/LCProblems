# 4 Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

## Examples
** Example 1:**
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

** Example 2:**
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```
## Constraints:
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`
## Solution

### Approach 1: Merge and Find Median
```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        vector<int> merged(n1 + n2);
        int i = 0, j = 0, k = 0;
        while (i < n1 && j < n2) {
            if (nums1[i] < nums2[j]) {
                merged[k++] = nums1[i++];
            } else {
                merged[k++] = nums2[j++];
            }
        }
        while (i < n1) {
            merged[k++] = nums1[i++];
        }
        while (j < n2) {
            merged[k++] = nums2[j++];
        }
        // Calculate median
        int total = n1 + n2;
        if (total % 2 == 1) {
            return merged[total / 2];
        } else {
            return (merged[total / 2 - 1] + merged[total / 2]) / 2.0;
        }
    }
};
```
**Complexity Analysis:**
- Time Complexity: `O(m + n)`, where `m` and `n`
are the lengths of `nums1` and `nums2` respectively. This is because we traverse both arrays once to merge them.
- Space Complexity: `O(m + n)` for storing the merged array.
### Approach 2: Binary Search
```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int n1 = nums1.size();
        int n2 = nums2.size();
        int low = 0, high = n1;
        while (low <= high) {
            int partition1 = (low + high) / 2;
            int partition2 = (n1 + n2 + 1) / 2 - partition1;

            int maxLeft1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
            int minRight1 = (partition1 == n1) ? INT_MAX : nums1[partition1];

            int maxLeft2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
            int minRight2 = (partition2 == n2) ? INT_MAX : nums2[partition2];

            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if ((n1 + n2) % 2 == 0) {
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
                } else {
                    return max(maxLeft1, maxLeft2);
                }
            } else if (maxLeft1 > minRight2) {
                high = partition1 - 1;
            } else {
                low = partition1 + 1;
            }
        }
    }
};
```
**Complexity Analysis:**
- Time Complexity: `O(log(min(m, n)))`, where `m` and `n` are the lengths of `nums1` and `nums2` respectively. This is because we perform binary search on the smaller array.
- Space Complexity: `O(1)` since we are using a constant amount of extra space.