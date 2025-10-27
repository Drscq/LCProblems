# 207 Course Schedule

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = `$[a_i, b_i]$ indicates that you must take course $b_i$ before course `$a_i$.

* For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

## Examples

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you
should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```
## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a_i, b_i < numCourses`
- All the pairs `prerequisites[i]` are unique.

## Solution

### Approach: Depth-First Search (DFS) for Cycle Detection
To determine if all courses can be finished, we can model the problem as a directed graph where each course is a node and each prerequisite relationship is a directed edge. The task then becomes checking if there is a cycle in this directed graph. If there is a cycle, it means that there is no way to complete all courses.

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses, 0); // 0 = unvisited, 1 = visiting, 2 = visited

        // Build the graph
        for (const auto& pre : prerequisites) {
            graph[pre[1]].push_back(pre[0]);
        }

        // DFS function to detect cycles
        function<bool(int)> dfs = [&](int course) {
            if (visited[course] == 1) return false; // cycle detected
            if (visited[course] == 2) return true;  // already visited

            visited[course] = 1; // mark as visiting
            for (int neighbor : graph[course]) {
                if (!dfs(neighbor)) return false;
            }
            visited[course] = 2; // mark as visited
            return true;
        };

        for (int i = 0; i < numCourses; ++i) {
            if (!dfs(i)) return false;
        }
        return true;
    }
};
```