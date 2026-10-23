
class LRUCache {
private:
    int capacity;
    list<pair<int, int>> cache;
    unordered_map<int, list<pair<int, int>>::iterator> mp;

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }

    int get(int key) {
        if (mp.find(key) == mp.end()) {
            return -1;
        }

        // Move the accessed key to the front
        auto it = mp[key];
        int value = it->second;

        cache.erase(it);
        cache.push_front({key, value});
        mp[key] = cache.begin();

        return value;
    }

    void put(int key, int value) {
        // If key exists, remove its old entry
        if (mp.find(key) != mp.end()) {
            cache.erase(mp[key]);
            mp.erase(key);
        }

        // Insert the new or updated entry at the front
        cache.push_front({key, value});
        mp[key] = cache.begin();

        // Remove the least recently used key if over capacity
        if (cache.size() > capacity) {
            int lruKey = cache.back().first;
            cache.pop_back();
            mp.erase(lruKey);
        }
    }
};
