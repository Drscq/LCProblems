# 1570 Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class `SparseVector`:

* `SparseVector(nums)`: Initializes the object with the vector `nums`.
* `dotProduct(vec)`: Compute the dot product between the instance of *SparseVector* and `vec`.

A **sparse vector** is a vector that has mostly zero values, you should store the sparse vector efficietly and compute the dot product between two sparse vectors.

Follow up: What if only one of the vectors is sparse?

## Example 1:

```python
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
``` 
## Example 2:

```python
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
```

## Example 3:

```python
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
```

## Constraints:
* `n == nums1.length == nums2.length`
* `1 <= n <= ` $10^5$
* 0 <= `nums1[i], nums2[i]` <= $100$>


## Implementation
### Naive Approach
The naive approach is to use the List data structure to store the sparse vector and iterate through both vectors to compute the dot product. 

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i in range(len(vec.nums)):
            total += self.nums[i] * vec.nums[i]
        return total
      

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
```

```cpp
class SparseVector {
public:
    SparseVector(vector<int>& nums) {
        m_nums = nums;
        m_size = nums.size();
    }

    int dotProduct(SparseVector& vec) {
        int total = 0;
        for (int i = 0; i < m_size; ++i) {
            total += m_nums[i] * vec.m_nums[i];
        }
        return total;
    }
private:
    vector<int> m_nums;
    int m_size;
};
```

### Optimized Approach
A sparse vector can skip many zero values by storing only the indices of nonzero elements. This is efficient because the dot product then only multiplies entries that are actually nonzero in both vectors, cutting down on redundant operations and improving performance significantly when most values are zeros.
```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.dic[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for key in vec.dic:
            if key in self.dic:
                total += vec.dic[key] * self.dic[key] 

        return total

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
```

```cpp
class SparseVector {
public:
    SparseVector(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) {
                m_dic[i] = nums[i];
            }
        }
    }
    int dotProduct(SparseVector& vec) {
        int total = 0;
        for (const auto& [key, value] : vec.m_dic) {
            if (m_dic.find(key) != m_dic.end()) {
                total += value * m_dic[key];
            }
        }
        return total;
    }
private:
    unordered_map<int, int> m_dic;
};
```