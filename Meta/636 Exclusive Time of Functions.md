# 636 Exclusive Time of Functions

One a single-threaded CPU, we execute a program containing `n` functions. Each function has a unique ID between `0` and `n-1`.

Function calls are stored in a call stack: when a function call starts, its ID is puhsed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list of logs, where `logs[i]' represents the `i`-th log message formatted as a string: `"{function_id}:{"start" | "end"}:{timestamp}"`. For example, `"0:start:3"` means a function call with ID `0` started at the beginning of timestamp `3`, and `"1:end:2"` means a function call with ID `1` ended at the end of timestamp `2`. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for `2` time units and another call executing for `1` time unit, the exclusive time is `2 + 1 = 3`.

Return the exclusive time of each function in an array, where the value at the `i`-th index represents the exclusive time for the function with ID `i`.

## Examples
**Example 1:**
```
Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So, the exclusive time of function 0 is 2 + 1 = 3, and the exclusive time of function 1 is 4.
```
**Example 2:**
```
Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
Output: [8]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Function 0 starts again at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 starts again at the beginning of time 6, executes 1 unit of time, and ends at the end of time 6.
Function 0 starts again at the beginning of time 7, executes 1 unit of time, and ends at the end of time 7.
So, the exclusive time of function 0 is 2 + 4 + 1 + 1 = 8.
```
**Example 3:**
```
Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
Output: [7,1]
Explanation:
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursivel call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (intial call) resumes execution at the beginning of time 6 and executes for 2 units of time.
Function 1 starts at the beginning of time 6 and executes for 1 unit of time and ends at the end of time 6.
Function 0 resumes execution at the beginning of time 6 and executes for 2 units of time.
So, the exclusive time of function 0 is 2 + 4 + 1 = 7, and the exclusive time of function 1 is 1.
```
## Constraints:
- `1 <= n <= 100`
- `1 <= logs.length <= 500`
- `0 <= function_id < n`    
- `0 <= timestamp <= 10^9`
- `No two start events will happen at the same timestamp.`
- `No two end events will happen at the same timestamp.`
- `Each function has an "end" log for each "start" log.`

## Solution

### Approach: Stack Simulation
We can simulate the function calls using a stack to keep track of the currently executing functions. We will iterate through the logs and update the exclusive time for each function based on whether it is starting or ending.
```cpp
class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> result(n, 0);
        stack<int> st;
        int prevTime = 0;

        for (const string& log : logs) {
            stringstream ss(log);
            string idStr, type, timeStr;
            getline(ss, idStr, ':');
            getline(ss, type, ':');
            getline(ss, timeStr, ':');

            int id = stoi(idStr);
            int time = stoi(timeStr);

            if (type == "start") {
                if (!st.empty()) {
                    result[st.top()] += time - prevTime;
                }
                st.push(id);
                prevTime = time;
            } else {
                result[st.top()] += time - prevTime + 1;
                st.pop();
                prevTime = time + 1;
            }
        }
        return result;
    }
};
```