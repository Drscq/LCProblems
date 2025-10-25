# 1539. Kth Missing Positive Number 

Given an array `arr` of positive integers sorted in a strictly increasing order, and an integer `k`.

Return the `kth` positive integer that is missing from this array.


## Examples

**Example 1:**
```
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
```

**Example 2:**
```
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
```
## Constraints
- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 1000`
- `1 <= k <= 1000`
- `arr[i] < arr[j]` for `1 <= i < j <= arr.length`

## Solution

### Approach: Simulation
We can simulate the process of finding missing positive integers by iterating through the array and counting the missing numbers until we reach the `kth` missing number.
```cpp
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int missingCount = 0;
        int currentNum = 1;
        int index = 0;
        
        while (missingCount < k) {
            if (index < arr.size() && arr[index] == currentNum) {
                index++;
            } else {
                missingCount++;
                if (missingCount == k) {
                    return currentNum;
                }
            }
            currentNum++;   
        }
        return -1; // This line will never be reached
    }
};
```

#### Complexity Analysis
- **Time Complexity:** O(n + k), where n is the length of the array.
- **Space Complexity:** O(1) since we are using a constant amount of extra space

### Approach: set

```cpp
class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        unordered_set<int> arrSet(arr.begin(), arr.end());
        int missingCount = 0;
        int currentNum = 1;
        while (missingCount < k) {
            if (!arrSet.count(currentNum)) {
                ++missingCount;
            }
            ++currentNum;
        }
        return currentNum - 1;
    }
};
```

#### Complexity Analysis
- **Time Complexity:** O(n + k), where n is the length of the array.
- **Space Complexity:** O(n) due to the extra space used by the set.