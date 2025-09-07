# Find N Unique Integers Sum up to Zero

Given an integer `n`, return any array containing `n` unique integers such that they add up to `0`.`

### Example 1:

```
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
```
### Example 2:

```
Input: n = 3
Output: [-1,0,1]
```
### Example 3:
```
Input: n = 1
Output: [0]
```

### Constraints:
- `1 <= n <= 1000`


## Solution

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n == 1:
            res.append(0)
            return res
        sum_val = 0
        for i in range(1, n):
            sum_val += i
            res.append(i)
        
        res.append(-sum_val)
        return res
```

## Solution 2

### Intution

We start by placing the smallest $\lfloor -\frac{n}{2} \rfloor$ positive integers and their negatives into the array. At this point, their sum is 0.

- When `n` is even, the array already satisfies the requirements.
- When `n` is odd, we need to add one more element, which is `0`, to ensure the sum remains 0.


Thus, the $n$ numbers are all distinct and their sum is 0. This gives us an array that satisfies the requirements.

```python
class Solution:
    def sumZero(self, n : int) -> List[int]:
        res = []
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2 == 1:
            res.append(0)
        return res
```
