# 670 Maximum Swap

You are given an integer `num`. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.


## Example 1:
```
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
```
## Example 2:
```
Input: num = 9973
Output: 9973
Explanation: No swap.
```

## Constraints:
- `0 <= num <= 10^8`

# Solution

## Intuition
We have a non-negative integer, and we are allowed to swap exactly two digits at most once. The goal is to amke the integer as large as possible after that single swap.

## How to solve it
1. **Break the number into digits**
We first split the number into individual digits, with the least significant digit first. For example, for `num = 2736`, we would have the list `[6, 3, 7, 2]`.
2. **Find the best swap**
* Starting from the rightmost digit (the most significant digit), we check if there is a bigger digit to its left that we can swap with.
* If there is a larger digit, we pick the leftmost digit occurrence of the largest digit to swap. This ensures that we maximize the number.
* We perform this swap only once and stop immediately afterwards.
3. **Rebuild the number**
* After the swap, we rebuild the number from the list of digits and return it.

```c++
class Solution {
public:
   std::vector<int> extractDigits(int num) {
    std::vector<int> res;
    while (num) {
        int remainder = num % 10;
        res.emplace_back(remainder);
        num /= 10;
    }
    return res;
}
    int recoverNum(std::vector<int> elements) {
        int res = 0;
        for (int i = elements.size() - 1; i >= 0; --i) {
            res *= 10;
            res += elements[i];
        }
        return res;
    }
    int maximumSwap(int num) {
        int res;
        // step 1: get the digits values from num
        std::vector<int> elements = extractDigits(num);
        for (int i = elements.size() - 1; i >= 0; --i) {
            int max_val = elements[i];
            int max_val_index = i;
            for (int j = 0; j < i; ++j) {
                if (elements[j] > max_val) {
                    max_val = elements[j];
                    max_val_index = j;
                }
            }
            if (i != max_val_index) {
                swap(elements[i], elements[max_val_index]);
                break;
            }
        }


        return recoverNum(elements);
    }
};
```