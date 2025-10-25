# 528 Random Pick with Weight 

********

You are given a 0-indexed array of positive integers `w` where `w[i]` describes the weight of the `i`th index.

You need to implement the function `pickIndex()`, which randomly picks an index in the range `[0, w.length - 1]` (inclusive) and returns it. The probability of picking an index `i` is `w[i] / sum(w)`, where `sum(w)` is the sum of all the weights.

- For example, if `w = [1, 3]`, the probability of picking index `0` is `1/ (1 + 3) = 0.25` (25%), and the probability of picking index `1` is `3 / (1 + 3) = 0.75` (75%).

## Examples

**Example 1:**

```
Input:
["Solution","pickIndex"]
[[[1]],[]] // The first element of the input is the constructor, and the second element is the method call.
Output:
[null,0]
Explanation: Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return index 0 since there is only one element in w.
```
**Example 2:**

```
Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output:
[null,1,1,1,1,0]
Explanation:
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
.......
and so on.
```
## Constraints
- `1 <= w.length <= 10^4`
- `1 <= w[i] <= 10^5`
- `pickIndex` will be called at most `10^4` times.

## Solution

### Approach: Prefix Sum and Binary Search
To solve this problem, we can use the prefix sum technique combined with binary search. The idea is to create a prefix sum array where each element at index `i` represents the sum of weights from index `0` to `i`. This allows us to map a random number to an index based on the weights.

```cpp
class Solution {
public:
    vector<int> prefixSums;
    int totalSum;

    Solution(vector<int>& w) {
        totalSum = 0;
        for (int weight : w) {
            totalSum += weight;
            prefixSums.push_back(totalSum);
        }
    }

    int pickIndex() {
        int randomNum = rand() % totalSum + 1; // Generate a random number between 1 and totalSum
        // Binary search to find the index
        int left = 0, right = prefixSums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (prefixSums[mid] < randomNum) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```
### Complexity Analysis
- **Time Complexity:**
    - The constructor `Solution` takes O(n) time to build the prefix sum array, where n is the length of the weights array.
    - The `pickIndex` function takes O(log n) time due to the binary search
    - Overall, the time complexity for multiple calls to `pickIndex` is O(n + m log n), where m is the number of calls to `pickIndex`.
- **Space Complexity:**
    - The space complexity is O(n) for storing the prefix sum array.