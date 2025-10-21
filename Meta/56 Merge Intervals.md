# 56 Merge Intervals

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 

## Example 1
```markdown
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
``` 

## Example 2
```markdown
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

# Constraints
- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i < end_i <= 10^4`

# Solution

## Approach 1: Sorting 

### Intuition
If we sort the intervals by their `start` value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

### Algorithm

**First**, we sort the list as described. Then, we insert the first interval into our merged list and continue iterating each interval in turn as follows: 

1. If the current interval begins after the previous interval ends, then they do not overlap and we can append the current interval to the merged list.
2. Otherwise, they do overlap, and we merge them by updating the end of the previous interval if it is less than the end of the current interval.

#### A concise, corrected proof

**Claim**:

After sorting by left endpoint and sweeping once, merging whenever the current interval intersects the last one in the output, the resulting list is exactly the set of maximal, pairwise-disjoint intervals that cover all original points.

**Proof**: Maintain an output list $O$.

For each input interval $x$ (visited in non-decreasing x.start), let y be the last interval in $O$.

(1) **Correctness of merging step:**
If x.start $\leq$ y.end, then $x \cup y = [y.start, \max(x.end, y.end)]$ covers both, so replacing $y$ with the union preserves the total covered set.

(2) **Disjointness of final list:** Assume, for contradiction, that the algorithm finishes with two intervals $a$ and $b$ in $O$ such that $a.end \geq b.start$. When $b$  was processed, $a$ was the last interval in $O$, and the test $b.start \leq a.end$. Hence, the algorithm would hhave merged $a$ and $b$, contradicting the assumption that $b$ was appended.

(3) **Minimality**: Because (2) shows every pair in $O$ is disjoint, no further merges are possible.


```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = []
        intervals.sort(key = lambda x : x[0])
        for interval in intervals:
            if not sorted_list or sorted_list[-1][1] < interval[0]:
                sorted_list.append(interval)
            else:
                sorted_list[-1][1] = max(sorted_list[-1][1], interval[1])
        return sorted_list
```

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> merged;
        sort(intervals.begin(), intervals.end());
        for (const auto& interval : intervals) {
            if (merged.empty() || merged.back()[1] < interval[0]) {
                merged.push_back(interval);
            } else {
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }
        return merged;
    }
};
```

### Complexity Analysis
* **Time Complexity**: $O(n \log n)$

Other than the `sort` invocation, we do a simple linear scan of the list, so the runtime is dominated by the sorting step.

* **Space Complexity**: $O(n)$ or $O(log n)$

If we sort `intervals` in place, we do not need more than constant additional space, although the sorting itself takes $O(n \log n)$ space. Otherwise, we must allocate linear space to store a copy of the intervals and sort that.