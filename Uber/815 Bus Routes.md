# 815. Bus Routes

You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the $i^{th}$ bus repeats forever.

* For example, if `routes[0] = [1, 5, 7]`, this means that the $0^{th}$ bus travels in the sequence $1\to5\to7\to1\to5\to7\to1\cdots$ forever.

You will start at the bus stop `source` (You are not on any bus initially), and you want to go to the bus stop `target`. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from `source` to `target`. Return `-1` if it is not possible.


## Example
**Example 1**
```
Input: routes = [[1, 2, 7], [3, 6, 7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
```

**Example 2**
```
Input: routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
source = 15, target = 12
Output: -1
```

## Constraints

* $1 \leq routes.length \leq 500$
* $1 \leq routes[i].length \leq 10^5$
* All the values of `routes[i]` are unique.
* $sum(routes[i].length) \leq 10^5$
* $0 \leq routes[i][j] < 10^6$
* $0 \leq source, target < 10^6$

## Solution

### Core Insight

The key insight is to not BFS over stops, but over bus routes. Each "step" in BFS represents boarding one bus. From any stop, you can board every bus that visits it, which then unlocks all stops on that bus route. You want the minimum number of buses taken to reach `target`.

### Algorithm
```c++
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target) return 0;

        auto stopToBuses = buildStopToBuses(routes);
        if (!isReachable(stopToBuses, source, target)) return -1;
        return bfs(routes, stopToBuses, source, target);
    }
    // step 1: build inverted index : stop -> list of bus indices passing through it
    unordered_map<int, vector<int>> buildStopToBuses(const vector<vector<int>>& routes) {
        unordered_map<int, vector<int>> stopToBuses;
        for (int busIdx = 0; busIdx < routes.size(); busIdx++) {
            for (int stop : routes[busIdx]) {
                stopToBuses[stop].emplace_back(busIdx);
            }
        }
        return stopToBuses;
    }
    // Step 2: Validate that source and target are reachable by at least one bus.
    bool isReachable(const unordered_map<int, vector<int>>& stopToBuses, int source, int target) {
        return stopToBuses.count(source) > 0 && stopToBuses.count(target) > 0;
    }
    // Step 3: BFS - expand by bus routes, counting buses taken per level.
    int bfs(const vector<vector<int>>& routes, const unordered_map<int, vector<int>>& stopToBuses, int source, int target) {
        queue<pair<int, int>> q; // {current stop, buses taken}
        unordered_set<int> visitedStops; // to avoid cycles in stops
        unordered_set<int> visitedBuses; // to avoid boarding the same bus twice
        q.push({source, 0});
        visitedStops.insert(source);
        while (!q.empty()) {
            auto [curStop, busesTaken] = q.front();
            q.pop();
            if (curStop == target) return busesTaken;
            for (int busIdx : stopToBuses.at(curStop)) {
                if (visitedBuses.count(busIdx) > 0) continue; // already boarded this bus
                visitedBuses.insert(busIdx);
                for (int nextStop : routes[busIdx]) {
                    if (!visitedStops.count(nextStop)) {
                        visitedStops.insert(nextStop);
                        q.push({nextStop, busesTaken + 1});
                    }
                }
            }
        }
        return -1; // target not reachable
    }
};
```

### Complexity Analysis
* Time Complexity: $O(N)$ where $N = \sum[routes[i]], since every stop and every bus bus is processed at most once.
* Space Complexity: $O(N)$ for the inverted index and visited sets.