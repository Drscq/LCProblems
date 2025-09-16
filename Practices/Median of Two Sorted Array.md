# Median of Two Sorted Arrays

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.


## Example 1:

```
Input : nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

## Example 2:

```
Input : nums1 = [1, 2], nums2 = [3,4]
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

### Intuition

We could improve the algorithm by performing the binary search only on the smaller array of `nums1` and `nums2`, thus the time complexity is reduced to `O(log(min(m,n)))`.

The main idea is to find a point of partition in both arrays such that the maximum of the smaller half is less than or equal to the minimum of the larger half.

However, instead of partitioning over the merged arrays, we can only focus on partitioning the smaller array (let's call this array `A`). Suppose the partition index is `partitionA`, we specify that the smaller half contains $(m + n + 1) / 2$ elements, and we can use this feature to our advantage by directly making `partitionB` equal to $(m + n + 1) / 2 - partitionA$. Thus, the smaller halves of both arrays contain a total of $(m + n + 1) / 2$ elements, as shown in the picture below.

![alt text](/Figures/Practices/MedianOfTwoSortedArrays/partitionAB.png)

The next step is to compare these edge elements.
- If `maxLeftA <= minRightB` and `maxLeftB <= minRightA` hold, it means that we have partitioned array at the correct place.

  - The smaller half consists of two sections `A_left` and `B_left`.
  - The larger half consists of two sections `A_right` and `B_right`.

We just need to find the maximum value from the smaller half as `max(maxLeftA, maxLeftB)` and the minimum value from the larger half as `min(minRightA, minRightB)`. The median value depends on these four boundary values and the total length of the input arrarys and we can compute it by situation.

- If `maxLeftA > minRightB`, it implies that maxLeftA is too large to be in the smaller half and we should look for a smaller partition value of `A`.

Otherwise, it denotes that `minRightA` is too small to be in the larger half and we should look for a larger partition value of `A`.


### Code

```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int m = nums1.size(), n = nums2.size();
        int low = 0, high = m;
        double res;
        while (low <= high) {
            int cut1 = (low + high) / 2;
            int cut2 = (m + n + 1) / 2 - cut1;
            int leftMax1 = (cut1 == 0) ? INT_MIN : nums1[cut1 - 1];
            int leftMax2 = (cut2 == 0) ? INT_MIN : nums2[cut2 - 1];

            int rightMin1 = (cut1 == m) ? INT_MAX : nums1[cut1];
            int rightMin2 = (cut2 == n) ? INT_MAX : nums2[cut2];
            
            if ((leftMax1 <= rightMin2) && (leftMax2 <= rightMin1)) {
                if ((m + n) % 2 == 0) {
                    return (max(leftMax1, leftMax2) + min(rightMin1,rightMin2 )) / 2.0;
                } else {
                    return  max(leftMax1, leftMax2);
                }
            } else if (leftMax1 > rightMin2) {
                high = cut1 - 1;
            } else {
                low = cut1 + 1;
            }
        }
        return 1.0;
        
    }
};
```