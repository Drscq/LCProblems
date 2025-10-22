# 347 Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```
**Example 3:**
```
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
```
**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

## Solution

### Approach 1: Hash Map + heap

```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> numFrequency;
        for (auto& num : nums) {
            numFrequency[num]++;
        }
        priority_queue<pair<int, int>> heap;
        for (auto& [num, frequency] : numFrequency) {
            heap.push({-frequency, num});
            if (heap.size() > k) {
                heap.pop();
            }
        }
        vector<int> res;
        while (!heap.empty()) {
            res.push_back(heap.top().second);
            heap.pop();
        }
        return res;
    }
};
```
#### Complexity Analysis
- Time complexity: O(N + U log k), where N is the size of the input array `nums` and U is the number of unique elements. Building the frequency map takes O(N), and maintaining a heap of size k while processing U unique elements takes O(U log k).
- Space complexity: O(N) for storing the frequency map. The heap takes O(k) space, but since k ≤ U ≤ N, the overall space complexity is O(N).