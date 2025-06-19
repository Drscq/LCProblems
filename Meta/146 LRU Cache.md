# 146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the `lRUCache` class:

* `lRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.

* `int get(int key)` Return the value of the `key` if the key exists,otherwise return -1.

* `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `get` and `put` must each run in $O(1)$ average time complexity.

## Example 1:
```
Input: 
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new lRUCache(2);
lRUCache.put(1, 1);       // cache is {1=1}
lRUCache.put(2, 2);       // cache is {1=1, 2=2}
lRUCache.get(1);          // return 1
lRUCache.put(3, 3);       // LRU key was 2, evict key 2, cache is {1=1, 3=3}
lRUCache.get(2);          // returns -1 (not found)
lRUCache.put(4, 4);       // LRU key was 1, evict key 1, cache is {4=4, 3=3}
lRUCache.get(1);          // returns -1 (not found)
lRUCache.get(3);          // returns 3
lRUCache.get(4);          // returns 4  
```

## Constraints:
* `1 <= capacity <= 3000`
* `0 <= key <= 10000`
* `0 <= value <= 100000`
* At most 2 * 10^5 calls will be made to `get` and `put`.


# Solution
## Intuition
The goal of an LRU (Least Recently Used) cache is to keep track of the most recently used items  so that when the cache reaches its capacity, it can efficiently remove the least recently used item. 

To achieve this, we use three key data structures:

1. `unorded_map<int, int> cache_map` stores the actual key-value pairs, giving us constant-time lookups.

2. `list<int> cache_keys` keeeps track of the usage order of keys, with the front being the least recently used and the back being the most recently used.

3. `unordered_map<int, list<int>::iterator> cache_iter_map` allows us to quickly find and remove a key's position from the usage list in constant time.

When a key is accessed or inserted, we move it to the back of the list to mark it as the most recently used. If the key already exists, we simply update its value and refresh its position. If it is a new and the cache is full, we evict the oldest key (the front of the list) and insert the new key at the back.


```cpp
class LRUCache {
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        auto it = cache_map.find(key);
        // case 1: key is not in cache_map return -1
        if (it == cache_map.end()) return -1;
        // case 2: key is in cache_map: update the cache_map, cache_keys, cache_iter_map and return
        // promote the key to the most recently used
        cache_keys.erase(cache_iter_map[key]);
        cache_keys.push_back(key);
        cache_iter_map[key] = std::prev(cache_keys.end());
        return it->second;
    }
    
    void put(int key, int value) {
        auto it = cache_map.find(key);
        // case 1: key exists in cache_map and then update the cache_map
        if (it != cache_map.end()) {
            cache_map[key] = value;
            // promote the key to the most recently used
            cache_keys.erase(cache_iter_map[key]);
            cache_keys.push_back(key);
            cache_iter_map[key] = std::prev(cache_keys.end());
            return;
        }
        // case 2: size of the cache_map = capacity and then do the eviction
        if (cache_map.size() == this->capacity) {
            auto key_evicted = cache_keys.front();
            cache_keys.pop_front();
            cache_map.erase(key_evicted);
            cache_iter_map.erase(key_evicted);
        }

        // add the key-value pair to the cache_map and update the cache_keys and cache_iter_map
        cache_map[key] = value;
        cache_keys.push_back(key);
        cache_iter_map[key] = std::prev(cache_keys.end());
    }

    int capacity;
    unordered_map<int, int> cache_map;
    list<int> cache_keys;
    unordered_map<int, list<int>::iterator> cache_iter_map;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
 ```
 