# 875 Koko Eating Bananas
**Medium**

Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas.
The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during that hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Examples
**Example 1:**
```
Input: piles = [3,6,7,11], h = 8
Output: 4
```
**Example 2:**
```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```
**Example 3:**
```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```
## Constraints
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`


## Solution

### Approach: brute force
```cpp
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int n = piles.size();
        int k = 1;
        while (eatingTime(piles, k) > h) {
            ++k;
        }
        return k;
    }
    long long eatingTime(vector<int>& piles, int k) {
        long long hours = 0;
        for (auto& pile : piles) {
            hours += ((pile + k - 1) / k);
        }
        return hours;
    }
};
```
### Approach: binary search
```cpp
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1, right = *max_element(piles.begin(), piles.end());
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (eatingTime(piles, mid) > h) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
    long long eatingTime(vector<int>& piles, int k) {
        long long hours = 0;
        for (auto& pile : piles) {
            hours += ((pile + k - 1) / k);
        }
        return hours;
    }
};
```

### Approach: dynamic programming
```cpp
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int n = piles.size();
        vector<int> dp(h + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i <= h; ++i) {
            for (int j = 0; j < n; ++j) {
                int k = (piles[j] + i - 1) / i;
                dp[i] = min(dp[i], max(dp[i - 1], k));
            }
        }
        return dp[h];
    }
};
``` 

