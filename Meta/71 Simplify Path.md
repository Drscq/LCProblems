# 71 Simplify Path
**Medium**
**Prepareation for next month's interview**

You are given an absolute path for a Unix-style file system, which always begins with a slash `/`. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

- A single dot `.` represents the current directory.

- A double dot `..` represents the previous/parent directory.

- Multiple consecutive slashes `//` and `///` are treated as a single slash `/`.

- Any sequence of periods that does not match the rules above should be treated as a valid directory  or file name. For example, `...` and `....` are valid directory or file names.

The simplified canonical path should follow these rules:

* The path must start with a single slash `/`.
* Directories within the path must be separated by exactly one slash `/`.

* The path must not end with a slash `/` unless it is the root directory `/`.
* The path must not have any single or double periods (`.` or `..`) used to denote current or parent directories.

Return the simplified canonical path.

## Examples

**Example 1:**

```
Input: path = "/home/"
Output: "/home"
Explanation: The trailing slash should be removed.
```
**Example 2:**

```
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: Multiple consecutive slashes are replaced by a single one.
```
**Example 3:**
```
Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"
Explanation: A double period ".." refers to the directory up a level (the parent directory).
```
**Example 4:**
```
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is not possible.
```
**Example 5:**
```
Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
Explanation: The sequence "..." is treated as a valid directory name.
```

## Constraints
- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `.`, slash `/`, or underscore `_`.
- `path` is a valid absolute Unix path.

## Solution

### Approach 1: Stack
```c++
class Solution {
public:
    string simplifyPath(string path) {
        vector<string> st;
        stringstream ss(path);
        string temp;
        while (getline(ss, temp, '/')) {
            if (temp == "" || temp == ".") continue;
            if (temp == "..") {
                if (!st.empty()) st.pop_back();
            } else {
                st.push_back(temp);
            }
        }
        string res = "/";
        for (int i = 0; i < st.size(); i++) {
            res += st[i];
            if (i != st.size() - 1) res += "/";
        }
        return res;
    }
};
```

```c++
class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        stringstream ss(path);
        string temp;
        while (getline(ss, temp, '/')) {
            if (temp == "" || temp == ".") continue;
            if (temp == "..") {
                if (!st.empty()) st.pop();
            } else {
                st.push(temp);
            }
        }
        string res = "/";
        vector<string> tempVec;
        while (!st.empty()) {
            tempVec.push_back(st.top());
            st.pop();
        }
        reverse(tempVec.begin(), tempVec.end());
        for (int i = 0; i < tempVec.size(); i++) {
            res += tempVec[i];
            if (i != tempVec.size() - 1) res += "/";
        }
        return res;
    }
};
```
### Complexity Analysis
- Time Complexity: O(N), where N is the length of the input path. We traverse
    the path string once to split it into components and process each component.
- Space Complexity: O(N), in the worst case, we may store all components of the path in the stack.