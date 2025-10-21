# Find First and Last Position of Element in Sorted Array

Given a sorted array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Example

### Example 1
```markdown
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
``` 
### Example 2
```markdown
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

## Constraints
* $0 \leq nums.length \leq 10^5$
* $-10^9 \leq nums[i] \leq 10^9$
* `nums` is a non-decreasing array.
* $-10^9 \leq target \leq 10^9$

## Solution

### Overview

Let's briefly look at a brute-fore way of solving this problem. Given a target element, we can simply do a linear scan over the entire array to find the first and last position. The first occurrence will be the first time when we encounter this target. Thereafter, we continue to scan elements until we find one that is greater than the target or until we reach the end of the array. This will help us determine the last position of the target.

The downside of this approach is that it does not take advantage of the sorted nature of the array. This linear scan approach has a time complexity of $O(n)$ because there are $n$ elements in the array. That does not sound too bad, right?Well, it does if we compare it to an approach with logarithmic time complexity. We will look at a binary search-based approach to solve this problem which will take advantage of the sorted nature of the array.


### Approach: Binary Search

#### Intuition

Let's review binary search a bit. Given a sorted array, binary search works by looking at the middle element of the given array, and based on the value of the middle element, it decides to discard one half of the array. At each step, we reduce the length of the array to search by half and that is what leads to the logarithmic time complexity of the algorithm. Usually, we employ the binary search algorithm to determine if an element is in a sorted array. Here, we can tweak the binary search algorithm to find the first and last position of a given element.

Let's look at the basic binary search algorithm one step at a time:

* We use 2 variables to keep track of the subarray that we are scanning. Let's call them `begin` and `end`. Initially, `begin` is set to $0$ and `end` is set to the last index of the array, which is `nums.length - 1`.
* We iterate until `begin` is greate than `end`.
* At each step, we calculate the middle element's index as `mid = (begin + end) // 2`. We use the value of the middle element to decide which half of the array we need to search next.

    * If the target that we are searching for has a value lower than the middle element, we discard the right half of the array i.e., we set `end = mid - 1`.
    * If the target that we are searching for has a value higher than the middle element, we discard the left half of the array i.e., we set `begin = mid + 1`.
    * If the target is equal to the middle element, we found our target and we return from there.

#### Binary Search and Bidirectional Scan

A naive way to use binary search to find the first and last position of a target is to first determine the index of any occurrence of the given target. Suppose we know that the target is at index `i` in the array. From there on, we do a linear scan to the left and keep going until we find the first occurrence of the target. Similarly, we do a linear scan to the right to find the last position. This works just fine. However, in the worst case, when our entire array is filled with the target valu, then this is a linear-time algorithm. In that case, the linear scan will end up taking more time than the binary-search itself.

#### Two Binary Searches

Instead of using a linear-scan approach to find the boundaries once the target has been found, let's use binary search again to find the first and last position of the target. We can make a small tweak to the checks we perform on the middle element. This tweak will help us determine the first and last position of an element.

Normally, we compare `nums[mid] == target` because we simply need to check if we found our target or not. But now, apart from checking for equality, we also need to check if `mid` is the first or the last index where the target occurs. Let's see how we can do that.

**Implementation**
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int, start: int, end: int) -> int:
            if end < start:
                return -1 
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            res = -1
            if nums[mid] > target:
                res = binarySearch(nums, target, start, mid - 1)
            else:
                res = binarySearch(nums, target, mid + 1, end)
            return res
        
        start = 0
        end = len(nums) - 1
        res = binarySearch(nums, target, start, end)
        if (res == -1):
            return [-1, -1]
        else:
            left_index = res - 1
            while left_index >= 0 and nums[left_index] == nums[res]:
                left_index -= 1
            right_index = res + 1
            while right_index < len(nums) and nums[right_index] == nums[res]:
                right_index += 1
            return [left_index + 1, right_index - 1]
```

##### First position in the array

There are two situations where an index will be the first occurrence of the target in the array.

1. If `mid` is the same as the `begin` which implies our `mid` element is the first element in the remaining subarray.

2. The element to the left of this index is not equal to the target that we are searching for i.e., `nums[mid - 1] != target`. If this condition is not met, we should keep searching on the left side of the array for the first occurrence of the target.

##### Last position in the array

There are two situations where an index will be the last occurrence of the target in the array.
1. If `mid` is the same as the `end` which implies our `mid` element is the last element of the remaining subarray.

2. If the element to the right of `mid` is not equal to the target we are searching for i.e., `nums[mid + 1] != target`. If this condition is not met, we should keep searching on the right side of the array for the last occurrence of the target.


#### Algorithm

1. Define a function called `findBound` which takes three arguments: the array `nums`, the `target` value, and a boolean `isFirst` which indicates whether we are looking for the first or last position of the target.

2. We use 2 variables to keep track of the subarray that we are scanning. Let's call them `begin` and `end`. Initially, `begin` is set to $0$ and `end` is set to the last index of the array, which is `nums.length - 1`.

3. We iterate until `begin` is greater than `end`.

4. At each step, we calculate the middle element `mid = (begin + end) // 2`. We use the value of the middle element to decide which half of the array we need to search next.
* nums[mid] == target:
    * isFirst is true: This implies that we are trying to find the first occurrence of the element. If `mid == begin` or `nums[mid - 1] != target`, then we return `mid` as the first occurrence of the `target`. Otherwise, we update `end = mid - 1`.
    * isFirst is false: This implies we are trying to find the last occurrence of the element. If `mid == end` or `nums[mid + 1] != target`, then we return `mid` as the last occurrence of the target. Otherwise, we update `begin = mid + 1`.

* nums[mid] > target: We update `end = mid - 1` since we must discard the right side of the array as the middle element is greater than the target.

* nums[mid] < target: We update `begin = mid + 1` since we must discard the left side of the array as the middle element is less than the target.

5. We return a value of -1 at the end of our function which indicates that `target` was not found in the array.

6. In the main `searchRange` function, we first call `findBound` with `isFirst` set to `true` to find the first position of the target. If the first position is -1, we return `[-1, -1]` since the target is not present in the array. Otherwise, we call `findBound` with `isFirst` set to `false` to find the last occurrence and then return the result.

**Implementation**
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchBound(nums: List[int], target: int, isFirst: bool) -> int:
            start = 0
            end = len(nums) - 1
            while start <= end:
                middle = (start + end) // 2
                if isFirst:
                    if nums[middle] == target and (middle == start or (middle - 1 >= 0 and nums[middle - 1] != target)):
                        return middle
                    if nums[middle] >= target:
                        end = middle -1
                    else:
                        start = middle + 1

                if not isFirst:  
                    if nums[middle] == target and (middle == end or (middle + 1 < len(nums) and nums[middle + 1] != target)):
                        return middle
                    if nums[middle] > target:
                        end = middle -1
                    else:
                        start = middle + 1
            return -1
        
        res_l = searchBound(nums, target, True)
        if res_l == -1:
            return [-1, -1]
        else:
            res_r = searchBound(nums, target, False)
            return [res_l, res_r]
```

### Approach 2 : Iterative Binary Search 
```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                int start = mid - 1;
                while (start >= 0 && nums[start] == target) {
                    start--;
                }
                int end = mid + 1;
                while (end < nums.size() && nums[end] == target) {
                    end++;
                }
                return {start + 1, end - 1};
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return {-1, -1}; // Placeholder return statement
    }
};
```