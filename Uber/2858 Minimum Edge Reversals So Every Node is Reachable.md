# 2858 Minimum Edge Reversals So Every Node is Reachable

There is a simiple directed graph with `n` nodes labeled from `0` to `n-1`. The graph would form a tree if its edges were bi-directional.

You are given an integer `n` and a 2D integer array `edges`, where `edges[i] = `[$u_i$, $v_i$] represents a directed edge going from node $u_i$ to node $v_i$. 

An edge reversal changes the direction of an edge, i.e., a directed edge going from node $u_i$ to node $v_i$ becomes a directed edge going from node $v_i$ to node $u_i$.

For every node `i` in the range `[0, n-1]`, your task is to independently calculate the minimum number of edge reversals required so it is possible to reach any other node starting from node `i` through a sequence of directed edges.

Return an integer array `answer`, where `answer[i]` is the minimum number of edge reversals required so it is possible to reach any other node starting from node `i` through a sequence of directed edges.

## Examples

### Example 1:
![alt text](/Figures/Uber/directed_graph_2858.png)

```
Input: n = 4, edges = [[2,0],[2,1],[1,3]]
Output: [1,1,0,2]
Explanation: The image above shows the graph formed by the edges.
For node 0: after reversing the edge [2,0], it is possible to reach any other node starting from node 0. So, answer[0] = 1.
For node 1: after reversing the edge [2,1], it is possible to reach any other node starting from node 1. So, answer[1] = 1.
For node 2: it is already possible to reach any other node starting from node 2. So, answer[2] = 0.
For node 3: after reversing the edges [1,3] and [2,1], it is possible to reach any other node starting from node 3. So, answer[3] = 2.
```

## Constraints

- $2 \leq n \leq 10^5$
- `edges.length == n-1`
- `edges[i].length == 2`
- $0 \leq u_i == edges[i][0] < n$
- $0 \leq v_i == edges[i][1] < n$
- $u_i != v_i$
- The input is generated such that if the edges were bi-directional, they would form a tree.


## Solution
This is a classic **Rerooting DP** (also called "tree DP with rerooting") problem. Here is a complete walkthrough.

### Core Insight
Since the graph forms a tree when edges undirected, there is exactly one path between any two nodes. The problem reduces to : for each possible root node, how many edges point "the wrong way" (toward the root instead of away)?

The naive approach - run BFS/DFS from every node - is $O(n^2)$, and will TLE (Time Limit Exceeded). Rerooting DP does it in $O(n)$ with two DFS traversals.

#### Graph Representation

Build an undirected adjacency list with edge weights encoding reversal cost:

- For original edge $u \to v$: store `adj[u] = {v, 0}` (free to traverse) and `adj[v] = {u, 1}` (cost 1 reversal to go backwards).

1. **Phase 1: Root DFS (compute `dp[]`)**

Root the tree at node `0`. Define `dp[x]` = min reversals for node `x` to reach every node in its subtree.

For each parent `x` with child `y`:

$$
dp[x] = \sum_{y \in children(x)}(dp[y] + cost(x \to y))
$$
Where $cost(x \to y)$ is `0` if edge is $x \to y$ and `1` if edge is $y \to x$.

2. **Phase 2: Reroot DFS (compute `answer[]`)**

`answer[0] = dp[0]` (already computed). The propagate downward: when shifting the root from parent `x` to child `y`:

If original edge is $x \to y$ (now need to reverse it for $y \to x$),
$$
answer[y] = answer[x] + 1 
$$

If original edge is $y \to x$ (was costly for $x$, now free for $y$),

$$
answer[y] = answer[x] - 1
$$

3. Walkthrough on Example 1:

`n = 4, edges = [[2,0],[2,1],[1,3]]`, tree rooted at 0: $0 \gets 2 \to 1 \to 3$.

3.1 **Phase 1**:

| Node | Children | Edge Direction | dp Value |
|------|----------|-------------|---------|
| 3 | none | --- | 0 |
| 1 | 3 | $1 \to 3$ (cost 0) | 0 + 0 = 0 |
| 2 | 1 | $2 \to 1$ (cost 0) | 0 + 0 = 0 |
| 0 | 2 | $2 \to 0$ (cost 1) | 0 + 1 = 1 |


3.2 **Phase 2**:

- `answer[0] = dp[0] = 1`
- $0 \to 2$: original edge is $2 \to 0$ (cost was 1), so `answer[2] = answer[0] - 1 = 0`
- $2 \to 1$: original edge is $2 \to 1$ (cost was 0), so `answer[1] = answer[2] + 1 = 1`
- $1 \to 3$: original edge is $1 \to 3  $ (cost was 0), so `answer[3] = answer[1] + 1 = 2`

### Code Implementation

```c++
class Solution {
public:
    vector<int> minEdgeReversals(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].emplace_back(e[1], 0); // original direction: free
            adj[e[1]].emplace_back(e[0], 1); // reverse direction: cost 1
        }

        vector<int> dp(n, 0), answer(n, 0);

        // Phase 1: Root DFS
        function<void(int, int)> dfs1 = [&](int node, int parent) {
            for (auto& [next, cost] : adj[node]) {
                if (next == parent) continue;
                dfs1(next, node);
                dp[node] += dp[next] + cost;
            }
        };
        dfs1(0, -1);

        // Phase 2: Rerooting to compute answer
        answer[0] = dp[0];
        function<void(int, int)> dfs2 = [&](int node, int parent) {
            for (auto& [next, cost] : adj[node]) {
                if (next == parent) continue;
                answer[next] = answer[node] + (cost == 0 ? 1 : -1); // adjust based on edge direction
                dfs2(next, node);
            }
        };
        dfs2(0, -1);
        return answer;  
    }
};
```

### Complexity Analysis
- Time Complexity: $O(n)$, since we perform two DFS traversals over the tree.
- Space Complexity: $O(n)$ for the adjacency list and DP arrays.

The key mental model is `dp[node]` tells you the cost from a fixed root downward; rerooting propagates how that cost shifts as you slide the "root" across each edge.


#### Modulization Version

```c++
class Solution {
public:
    vector<int> minEdgeReversals(int n, vector<vector<int>>& edges) {
        // adjacency list with edge costs
        vector<vector<pair<int, int>>> adj = buildGraph(n, edges);
        // First DFS to get the min reversals from root
        vector<int> dp(n, 0);
        dfs1(0, -1, adj, dp);
        // Second DFS to reroot and get answers for all nodes
        vector<int> answer(n, 0);
        answer[0] = dp[0];
        dfs2(0, -1, adj, answer);
        return answer;
    }
    vector<vector<pair<int, int>>> buildGraph(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].emplace_back(e[1], 0);
            adj[e[1]].emplace_back(e[0], 1);
        }
        return adj;
    }
    void dfs1(int node, int par, vector<vector<pair<int, int>>>& adj, vector<int>& dp) {
        for (auto& [next, cost] : adj[node]) {
            if (next == par) continue;
            dfs1(next, node, adj, dp);
            dp[node] += dp[next] + cost;
        }
    }

    void dfs2(int node, int par, vector<vector<pair<int, int>>>& adj, vector<int>& answer) {
        for (auto& [next, cost] : adj[node]) {
            if (next == par) continue;
            answer[next] = answer[node] + (cost == 0 ? 1 : -1);
            dfs2(next, node, adj, answer);
        }
    }
};
```