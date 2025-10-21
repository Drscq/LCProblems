# 973. K Closest Points to Origin.

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance(i.e., t$\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## Example 1:
```markdown
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation: The distance between (1, 3) and the origin is sqrt((1-0)^2 + (3-0)^2) = sqrt(10).
The distance between (-2, 2) and the origin is sqrt((-2-0)^2 + (2-0)^2) = sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only need to return one of the two closest points to the origin, so return [[-2,2]].
``` 

## Constraints:
- `1 <= k <= points.length <= 10^4`
- `-10^4 < xi, yi < 10^4`

# Solution

## Approach 2: Max Heap or Max Priority Queue

### Intuition
While we must iterate over all elements in the points array, we only need to keep track of the k closest points encountered so far. We could therefore choose to store them in a separate data structure. In order to keep this data structure capped at k elements, we will need to keep track of the point that is farthest away from the origin and thus the next point to be removed when a closer point is found.

The ideal data structure for this purpose is a max heap or max priority queue. These data structures allow access to the max value in constant time and perform replacements in logarithmic time.

Note: We can simulate max heap functionality in a min heap data structure by inserting −dist instead of dist, if necessary.

At the start of our iteration through points, we will insert the first k elements into our heap. Once the heap is "full", we can then compare each new point to the farthest point stored in the heap. If the new point is closer, then we should remove the farthest point from the heap and insert the new point.

After the entire points array has been processed, we can create an array from the points stored in the heap and then return the answer.

Algorithm

* Use a max heap (or max priority queue) to store points by distance.
    * Store the first k elements in the heap.
    * Then only add new elements that are closer than the top point in the *heap while removing the top point to keep the heap at k elements.
* Return an array of the k points stored in the heap.

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            distance = x**2 + y**2
            heapq.heappush(heap, (distance, point))
        
        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res
```


```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> maxHeap;
        for (const auto& point : points) {
            int x = point[0];
            int y = point[1];
            int distance = x * x + y * y;
            maxHeap.push({distance, point});
            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }
        vector<vector<int>> res;
        while (!maxHeap.empty()) {
            res.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return res;
    }
};
```     

**Just collecting the index in the heap instead of the vector**

```cpp
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, int>> maxHeap;
        for (int i = 0; i < points.size(); ++i) {
            int x = points[i][0];
            int y = points[i][1];
            int distance = x * x + y * y;
            maxHeap.push({distance, i});
            if (maxHeap.size() > k) {
                maxHeap.pop();
            }
        }
        vector<vector<int>> res;
        while (!maxHeap.empty()) {
            res.push_back(points[maxHeap.top().second]);
            maxHeap.pop();
        }
        return res;
    }
};
```

#### Complexity Analysis
* Time complexity: O(N log k), where N is the number of points. We iterate through all points, and each insertion and removal operation on the heap takes O(log k) time.
* Space complexity: O(k), the size of the heap.