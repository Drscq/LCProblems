# 202 Happy Number

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return `true` if `n` is a happy number, and `false` if not.

## Examples

**Example 1:**

```
Input: n = 19
Output: true
Explanation:
$1^2 + 9^2 = 82$
$8^2 + 2^2 = 68$
$6^2 + 8^2 = 100$
$1^2 + 0^2 + 0^2 = 1$
```
**Example 2:**

```
Input: n = 2
Output: false
Explanation: 2 is not a happy number.
```
## Constraints
- $1 <= n <= 2^{31} - 1$

## Solution

### Approach 1: Detect Cycle using HashSet

#### Intuition
A good way to get started with a question like this is to make a couple of examples. Let start with the number $7$. The next number will be $49$ (since $7^2 = 49$), and then the next after that will be $97$. We can continually repeat the process of squaring and then adding the digits until we get to 1. Because we got to 1, we know that $7$ is a happy number and the function should return `true`.
![alt text](/Figures/google/HapplyNumber/HappyNumberExample.png)

As another example, let's start with 116. By repeatedly applying the squaring and adding process, we eventually get to $58$, and then a bit after that we get back to $58$. Because we are back at a number we have already seen, we know there is a cycle, and therefore it is impossible to even reach $1$.  So for 116, the function should return `false`.
![alt text](/Figures/google/HapplyNumber/NotHappyNumberWithForLoop.png)

#### Implementation
```cpp
class Solution {
public:
    int getNext(int n) {
        int totalSum = 0;
        while (n > 0) {
            int d = n % 10;
            n = n / 10;
            totalSum += d * d;
        }
        return totalSum;
    }

    bool isHappy(int n) {
        unordered_set<int> seen;
        while (n != 1 && seen.find(n) == seen.end()) {
            seen.insert(n);
            n = getNext(n);
        }
        return n == 1;
    }
};
```
#### Complexity Analysis
- Time Complexity: $O(\log n)$, where $n$ is the input number
- Space Complexity: $O(\log n)$, the space used by the `seen`
