# 912 Sort an Array

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in $O(n log(n))$ time complexity and with the smallest space complexity possible.

## Examples 
**Example 1:**
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

**Example 2:**
```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```
## Constraints
- $1 <= nums.length <= 5 * 10^4$
- $-5 * 10^4 <= nums[i] <= 5 * 10^4$

## Solutions

### Overview
The purpose of this problem is to evaluate the interviewee's understanding of sorting algorithms and their ability to implement these algorithms without relying on built-in sort methods.

There are a variety of sorting algorithms such that Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort, Heap Sort, Quick Sort, Counting Sort, Radix Sort, and others. In this article, we will concentrate on four algorithms that are deemed efficient enough for this particular problem - Merge Sort, Heap Sort, Counting Sort, and Radix Sort.


#### Sorting Algorithm Time Complexities

| Algorithm       | Best Case        | Average Case      | Worst Case        |
|-----------------|------------------|-------------------|-------------------|
| Bubble Sort     | $O(n)$           | $O(n^2)$          | $O(n^2)$          |
| Insertion Sort  | $O(n)$           | $O(n^2)$          | $O(n^2)$          |
| Selection Sort  | $O(n^2)$         | $O(n^2)$          | $O(n^2)$          |
| Merge Sort      | $O(n\\log(n))$  | $O(n\\log(n))$   | $O(n\\log(n))$   |
| Heap Sort       | $O(n\\log(n))$  | $O(n\\log(n))$   | $O(n\\log(n))$   |
| Quick Sort      | $O(n\\log(n))$  | $O(n\\log(n))$   | $O(n^2)$          |
| Counting Sort   | $O(n + k)$       | $O(n + k)$        | $O(n + k)$        |
| Radix Sort      | $O(d(n + k))$    | $O(d(n + k))$     | $O(d(n + k))$     |



We attached a list of time complexities of some popular sorting algorithms. Here, $n$ is the number of elements in array, $k$ is the size of the buckets used, and $d$ is the number of maximum digits  of an element in the array.

#### Approach 1: Merge Sort
##### Intuition
Merge Sort is a divide-and-conquer sorting algorithm. The intuition behind it is to divide the data set into smaller and smaller sub-arrays until it is easy to sort, and then merge the sorted sub-arrays back into a larger sorted array.

The steps for implementing Merge Sort are as follows:

*  Divide the data set into two equal parts: The first step in the Merge Sort algorithm is to divide the data set into two equal halves. This is done by finding the middle point of the data set and splitting the data into two parts.

* Recursively sort each half: Once the data set has been divided into two halves, the Merge Sort Function is called recursively on each half. the recursive calls continue until each half of the data is sorted into single-element arrays.

* Merge the sorted halves: Once each half of the data is sorted, the two halves are merged back into one final sorted array. The merging process involves comparing the first element of each half and inserting the smaller element into the final array. This process is continues until one of the halves is empty. The remaining elements of the other half are then inserted into the final array.

* Repeat the process until the entire data is sorted: The Merge Sort function is called recursively until the entire data set is sorted.

![alt text](/Figures/google/SortAnArray/mergeSortExample.png)
##### Algorithm
1. Create a helper function called `merge` that takes in the original array `arr`, indices `left`, `mid`, `right`, and a temporary array `tempArr` as parameters.

    * Calculate the start indices and sizes of the two halves of the array. The first half starts from the `left` index and the second half starts from `mid + 1`.
    * Copy elements of both halves into the temporary array.
    * Merge the sub-arrays from the temporary array `tempArr` back into the original array `arr` in a sorted order using a while loop. The loop until either the first half or second half is completely merged. In each iteration, the smaller of the two elements from the first and second half is copied into the original array. "arr".
    * Copy any remaining elements from the first half or second half into the original array.

2. Create a recursive function called `mergeSort` which takes in the original array `arr`, indices `left`, `right`, and a temporary array `tempArr` as parameters.

    * Check if the `left` index is greater than or equal to the `right` index. If it is, we return from the funciotn.
    * Calculate the `mid` index.
    * Sort the first and second halves of the array recursively by calling the `mergeSort` function on each half.
    * Merge the sorted halves by calling the `merge` function.

3. Create a temporary array `temporaryArray` with the same size as the `nums` array.

4. Call the `mergeSort` function on the `nums` array with boundary, 0, and `nums.size() - 1`.

5. Return the sorted `nums` array.

##### Implementation

```cpp
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> tmpNums(n);
        mergeSort(nums, 0, n - 1, tmpNums);
        return nums;
    }
    void mergeSort(vector<int>& nums, int left, int right, vector<int>& tmpNums) {
        if (left >= right) return;
        int middle = (left + right) / 2;
        mergeSort(nums, left, middle, tmpNums);
        mergeSort(nums, middle + 1, right, tmpNums);

        merge(nums, left, middle, right, tmpNums);
    }
    void merge(vector<int>& nums, int left, int middle, int right, vector<int>& tmpNums) {
        int start1 = left;
        int start2 = middle + 1;
        int n1 = middle - left + 1;
        int n2 = right - start2 + 1;
        // copy the left side of nums to the tmpNums
        for (int i = 0; i < n1; ++i) {
            tmpNums[start1 + i] = nums[start1 + i];
        }
        // copy the right side of nums ot the tmpNums
        for (int i = 0; i < n2; ++i) {
            tmpNums[start2 + i] = nums[start2 + i];
        }

        int p1 = start1;
        int p2 = start2;
        int p = left;
        while (p1 < start1 + n1 && p2 < start2 + n2) {
            if (tmpNums[p1] <= tmpNums[p2]) {
                nums[p++] = tmpNums[p1];
                p1++;
            } else {
                nums[p++] = tmpNums[p2];
                p2++;
            }
        }
        while (p1 < start1 + n1) {
            nums[p++] = tmpNums[p1++];
        }
        while (p2 < start2 + n2) {
            nums[p++] = tmpNums[p2++];
        }

    }
};
```


##### Complexity Analysis
* Time Complexity: The time complexity of Merge Sort is $O(n \log(n))$
* Space Complexity: The space complexity of Merge Sort is $O(n)$ due to the temporary array used for merging.


