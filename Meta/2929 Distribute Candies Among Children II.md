# 2929. Distribute Candies Among Children II

## Problem Description
You are given two positive integers `n` and `limit`.

Return the total number of ways to distribute `n` candies among 3 children such that no child gets more than `limit` candies.

### Example 1:
```
Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
```

### Example 2
```
Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0), (3, 0, 0)
```

## Problem Solutions

**Intuition:** brute force all possible distributions of the candies and count the valid ones.
```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for x_1 in range(0, limit + 1):
            # x_1 denotes the number of candies got by first child
            for x_2 in range(0, limit+1):
                x_3 = n - (x_1 + x_2)
                if 0<= x_3 <=limit:
                    res += 1
        return res
```
You will get a Time Limit Exceeded (TLE) error for large inputs, so we need to optimize the solution.

**Optimized Approach:** The brute force solution can be made significantly more efficient by avoiding the innermost loop entirely and counting valid $x_2$ values directly using interval bounds.

We fix $x_1$ then compute the valid range of $x_2$ such that $x_3 = n - (x_1 + x_2)$ satisfies $0 <= x_3 <= limit$. This gives us a range for $x_2$:
$0 \leq n - (x_1 + x_2) \leq limit \to n - x_1 - limit \leq x_2 \leq n - x_1$.

**Interset** this with the domain of $x_2 \in [0, limit]$, and count the number of integer $x_2$ values in that interval.

```python
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for x_1 in range(0, limit + 1):
            low_bound_2 = max(0, n - x_1 - limit)
            high_bound_2 = min(limit, n - x_1)
            if low_bound_2 <= high_bound_2:
                res += (high_bound_2 - low_bound_2 + 1)
        return res
```

