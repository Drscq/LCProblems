# Alien Dictionary

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of string `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `""`.

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

## Examples

**Example 1:**

```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

**Example 2:**

```
Input: words = ["z","x"]
Output: "zx"
```
**Example 3:**

```
Input: words = ["z","x","z"]
Output: ""
```

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters.

## Solution

### Core Insight
By comparing adjacent words in the sorted list, you can extract ordering rules between characters. Then you need to find a valid ordering that satisfies all those rules, which is exactly what topological sort does.

**Step 1: Extract Character Order Rules**
Compare each pair of adjacent words. Find the first character that differs that tells you one character comes before another.

```
words = ["wrt","wrf","er","ett","rftt"]

"wrt" vs "wrf" -> t comes before f (t -> f)
"wrf" vs "er" -> w comes before e (w -> e)
"er" vs "ett" -> r comes before t (r -> t)
"ett" vs "rftt" -> e comes before r (e -> r)
```
⚠️ **Edge Case**: If word A is longer than word B, but B is a prefix of A (e.g., "abc" vs "ab"), then the order is invalid.

**Step 2: Build a Directed Graph**
Each rule `a->b` becomes a directed edge edge. Also track &**in-degrees** (how many edges point into each node).
```
Edges: t->f, w->e, r->t, e->r
Nodes (all unique chars): w, r, t, f, e
In-degrees: w = 0, r = 1, t = 1, f = 1, e = 1
```
**Step 3: Topological Sort(BFS/Kahn's Algorithm)**
- Start with all nodes that have in-degree 0 (nothing comes before them).
- Process each node, reducing neighbors' in-degrees.

- When a neighbor hits in-degree 0, add it to the queue.

- If you process all nodes -> valid order. If not -> cycle detected, return "".

### Implementation

```c++
class Solution {
public:
    string alienOrder(vector<string>& words) {
        vector<vector<bool>> graph(26, vector<bool>(26, false));
        vector<bool> seen(26, false);
        vector<int> indegree(26, 0);
        int uniqueCount = 0;
        collectChars(words, seen, uniqueCount);
        if (!buildGraph(words, graph)) return "";
        computeIndegree(graph, seen, indegree);
        return kahnTopologicalSort(graph, seen, indegree, uniqueCount);
    }
    // Collect all unique characters
    void collectChars(const vector<string>& words, vector<bool>& seen, int uniqueCount) {
        for (const string& word : words) {
            for (char c : word) {
                if (!seen[c - 'a']) {
                    seen[c - 'a'] = true;
                    uniqueCount++;
                }
            }
        }
    }
    // Build the graph based on adjacent word comparisons
    bool buildGraph(const vector<string>& words, vector<vector<bool>>& graph) {
        for (int i = 0; i + 1 < words.size(); ++i) {
            const string& a = words[i];
            const string& b = words[i + 1];
            int minLength = min(a.size(), b.size());
            bool foundDifference = false;
            for (int j = 0; j < minLength; ++j) {
                if (a[j] != b[j]) {
                    int u = a[j] - 'a';
                    int v = b[j] - 'a';
                    if (!graph[u][v]) return false; // Invalid order
                    graph[u][v] = true;
                    foundDifference = true;
                    break;
                }
            }
            // Edge case 'abc' vs 'ab' -> invalid
            if (!foundDifference && a.size() > b.size()) return false;
        }
        return true;
    }
    // Compute in-degrees for each node
    void computeIndegree(const vector<vector<bool>>& graph, const vector<bool>& seen, vector<int>& indegree) {
        for (int u = 0; u < 26; ++u) {
            for (int v = 0; v < 26; ++v) {
                if (u != v && seen[u] && seen[v] && graph[u][v]) {
                    indegree[v]++;
                }
            }
        }
    }         
    // Kahn's BFS Topological Sort
    string kahnTopologicalSort(const vector<vector<bool>>& graph, const vector<bool>& seen, vector<int>& indegree, int uniqueCount) {
        queue<int> q;
        for (int i = 0; i < 26; ++i) {
            if (seen[i] && indegree[i] == 0) {
                q.push(i);
            }
        }
        string result;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            result += (char)(u + 'a');
            for (int v = 0; v < 26; ++v) {
                if (v != u && seen[v] && graph[u][v]) {
                    if (--indegree[v] == 0) {
                        q.push(v);
                    }
                }
            }
        }
        // cycle detected if not all chars are processed 
        return result.size() == uniqueCount ? result : "";
    }
};
```

### Complexity Analysis
- Time Complexity: $O(N \cdot L + 26^2)$ where N = number of words, L = max word length.

- Space Complexity: $O(26^2)$ for the graph and $O(26)$ for in-degrees and seen arrays.


### Key Edge Cases to Remember

1. Prefix conflict: `["abc", "ab"]` should return `""` because the order is invalid.

2. Cycle detection: if `graph[v][u]` is already true when trying to add an edge `u->v`, it means there's a cycle, so return `""` or if Kahn's algorithm doesn't process all characters.

3. Multiple valid orders: any valid topological ordering is acceptable.