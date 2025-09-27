# 349 Intersection of Two Arrays

Given two integer array `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique and you can return the result in any order.

## Examples 

**Example 1:**
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

**Example 2:**
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
```
## Constraints
- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Solution

### Approach 1: Using Sets

```c++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1(nums1.begin(), nums1.end());
        unordered_set<int> resultSet;

        for (int num : nums2) {
            if (set1.count(num)) {
                resultSet.insert(num);
            }
        }
        return vector<int>(resultSet.begin(), resultSet.end());
    }
};
```


```c++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        if (n1 > n2) return intersection(nums2, nums1);
        unordered_set<int> set;
        for (auto& num1 : nums1) {
            for (auto& num2 : nums2) {
                if (num2 == num1) set.insert(num2);
            }
        }
        vector<int> ans;
        for (auto& val : set) {
            ans.push_back(val);
        }
        return ans;
    }
};
```