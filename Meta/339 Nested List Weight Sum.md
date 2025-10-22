# 339 Nested List Weight Sum

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is defined as the number of lists that it is inside of. For example, the nested list `[1,[2,2],[[3],2],1]` has each integer's value set to its depth.

Return the sum of each integer in `nestedList` multiplied by its depth.

## Examples
**Example 1:**
```
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1.
1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10
```
**Example 2:**
```
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3.
1*1 + 4*2 + 6*3 = 27
```
**Example 3:**
```
Input: nestedList = [0]
Output: 0
```

## Constraints
* 1 <= nestedList.length <= 50
* The values of the integers in the nested list in the range [-100, 100].
* The maximum depth of any integer in the nested list does not exceed 50.

## Solution

### Approach 1: Depth-First Search (DFS)
We can solve this problem using a depth-first search (DFS) approach. We will traverse the nested list recursively, keeping track of the current depth. For each integer we encounter, we will multiply it by its depth and add it to our total sum.
```cpp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    int depthSum(vector<NestedInteger>& nestedList) {
        return dfs(nestedList, 1);
    }

private:
    int dfs(const vector<NestedInteger>& nestedList, int depth) {
        int sum = 0;
        for (const auto& ni : nestedList) {
            if (ni.isInteger()) {
                sum += ni.getInteger() * depth;
            } else {
                sum += dfs(ni.getList(), depth + 1);
            }
        }
        return sum;
    }
};
```
### Complexity Analysis
* Time Complexity: O(N), where N is the total number of integers in the nested list
* Space Complexity: O(D), where D is the maximum depth of the nested list due to the recursion stack.