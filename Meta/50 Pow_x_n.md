# 50 Pow(x, n)

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

## Example 1
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

## Example 2
```
Input: x = 2.10000, n = 3
Output: 9.26100
```
## Example 3
```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
```

## Constraints

- $-100.0 < x < 100.0$
- $-2^{31} \leq n \leq 2^{31} - 1$
- `n` is an integer.
- Either `x` is not zero or `n` is a positive integer.
- $-10^4 \leq x^n \leq 10^4$


# Solution

## Approach 1: Binary Exponentiation (Recursive)

### Intuition

We know $x^n$ means we multiply $x$ with itself $n$ times. The most naive way to solve this problem is to simply multiply $x$ $n$-times. This method of multiplying will lead to a linear time complexity and is not efficient, but we will discuss a bit about it as it will be a stepping stone to our optimization approach.

#### Brute Force Approach

The current problem can be broken into smaller similar subproblems, $x^n = x \cdot x^{n-1}$. Thus, this will be our recurrence relation.

We can write a recursive function here that calculates the result of the smaller similar sub-problem and using that calculates the result for the current problem, $pow(x, n) = x \cdot pow(x, n-1)$. And we know if $n$ is $0$, then $pow(x, 0) = 1$, this will be our base case to stop the recursive calls.

Also, we need to handle the case if $n$ is negative. In that case, the answer will be the reciprocal of the result if $n$ were positive.

$x^{-n} = \frac{1}{x^n}$, where $n < 0$.

```python
def pow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    elif n < 0:
        return 1 / pow(x, -n)
    else:
        return x * pow(x, n - 1)
``` 

Now we have an idea of all cases.

### Optimized approach

Binary exponentiation, also known as exponentiation by squaring, is a technique for efficiently computing the power of a number. By repeatedly squaring $x$  and halving $n$, we can quickly compute $x^n$ in logarithmic number of multiplications.

The basic idea is to use the fact that $x^n$ can be expressed as 

* $(x^2)^{n/2}$ if $n$ is even, and
* $x \cdot (x^2)^{(n-1)/2}$ if $n$ is odd (we separate out one x, then n - 1 becomes even).


This method might not seem intuitive, so let's try to understand it with the help of some examples.

Say, we need to find $2^{100}$.

Using the previously dicussed recursive approach we will have to multiply $2$ in 100 steps.
Using the previously discussed recursive approach, we will have to multiply `2` in 100 steps:

```
2^100 = 2 * 2^99
    = 2 * 2 * 2^98
    = 2 * 2 * 2 * 2^97
    ...
    (100 steps)
    ...
    = 2 * 2 * ... * (100 multiplications) ... * 2^0
    = 1267650600228229401496703205376
```

But using the binary exponentiation, it will be reduced to about only 10 steps.

```
2^100 = (2^2)^50
    = 4^50
    = (4^2)^25
    = 16^25
    = 16 * (16^24)
    = 16 * (16^2)^12
    = 16 * 256^12
    = 16 * (256^2)^6
    = 16 * 65536^6
    = 16 * (65536^2)^3
    = 16 * 4294967296^3
    = 16 * 4294967296 * (4294967296^2)
    = 16 * 4294967296 * (4294967296^2)^1
    = 1267650600228229401496703205376
```

Instead of reducing the exponent $n$  by $1$ at each recursive call like in the brute-force method, we will reduce it by half here. Thus, instead of linear steps, it will take us logarithmic steps to perform all the multiplications.


#### Algorithm

1. Create a method `binaryExp`, which takes `x` and `n` as parameters.
    * If `n` is 0, return 1.
    * If `n` is negative, return `1 / binaryExp(x, -n)`.
    * If `n` is even, return `binaryExp(x * x, n / 2)`.
    * If `n` is odd, return `x * binaryExp(x * x, (n - 1) / 2)

2. Call the `binaryExp` method with `x` and `n`.


#### Implementation

```python
class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        # Base case, to stop recursive calls.
        if n == 0:
            return 1

        # Handle case where, n < 0.
        if n < 0:
            return 1.0 / self.binaryExp(x, -1 * n)

        # Perform Binary Exponentiation.
        # If 'n' is odd we perform Binary Exponentiation on 'n - 1' and multiply result with 'x'.
        if n % 2 == 1:
            return x * self.binaryExp(x * x, (n - 1) // 2)
        # Otherwise we calculate result by performing Binary Exponentiation on 'n'.
        else:
            return self.binaryExp(x * x, n // 2)

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)
```

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        
        if n % 2 == 1:
            return x * self.myPow(x * x, (n-1) / 2)
        else:
            return self.myPow(x * x, n/2)
```


## Complexity Analysis

* Time Complexity: $O(\log n)$

    * At each recursive call we reduce `n` by half, so we will make only $O(\log n)$ number of calls for the `binaryExp` method, and the multiplication of two numbers is considered as a constant time operation.
    * Space Complexity: $O(\log n)$

Note: The standard multiiplication algorithm for multiplying two numbers of $d$-digits takes $O(d^2)$ time, but most modern programming languages achieve a much lower time complexity i.e., $O(d (\log d)(\log \log d))$ by utilizing a divide-and-conquer strategy and leveragin fast fourier transform (FFT) algorithms. However, for simplicity, we consider it as $O(1)$ in this context

* Space Complexity: $O(\log n)$

    * The space complexity is due to the recursive call stack, which can go up to $O(\log n)$ in depth.



## Approach 2: Recursive

```cpp
class Solution {
public:
    double myPow(double x, long long n) {
        if (n == 0) return 1.0;
        if (n < 0) return 1.0 / myPow(x, -n);
        
        if (n % 2 == 1) {
            return x * myPow(x * x, (n - 1) / 2);        
        } else {
            return myPow(x * x, n / 2);
        }

        return 1.0;
    }
};
```