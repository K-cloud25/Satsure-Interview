🧠 LRUCache — Thread-Safe Cache with TTL Support
A thread-safe, TTL-enabled Least Recently Used (LRU) cache implementation in Python, supporting both object-based and context-managed usage patterns.

🚀 How to Run the Code
🧪 Run Unit Tests
Run specific test modules:

bash
Copy
Edit
python -m unittest tests/concurr
python -m unittest tests/arbitart
🔧 Using the LRUCache
1. Object-Based Instantiation
python
Copy
Edit
from models.LRUCache import LRUCache

cache = LRUCache(max_size=4)

cache.put("key1", "value1", ttl=60)
value = cache.get("key1")
stats = cache.get_stats()
cache.clear()
cache.stop()  # IMPORTANT: Clean up background threads
2. Context-Based Instantiation
python
Copy
Edit
from models.LRUCache import LRUCache

with LRUCache(max_size=4) as cache:
    cache.put("key2", "value2")
    print(cache.get("key2"))
# `stop()` is automatically called on exit
📦 Dependencies
Python 3.13.1

Standard library only (no external packages required)

⚙️ Design Decisions
📚 Data Structures
Structure	Purpose
deque	Maintains access order (LRU logic) — oldest key at front
dict	Stores key-to-CacheItem mappings for O(1) lookups

🧵 Concurrency Model
Global threading.Lock ensures thread-safe access to queue and map.

Daemon background thread handles TTL-based key expiration.

Thread-safe statistics tracking via Stats class.

♻️ Eviction Logic
1. Size-Based Eviction
If cache.size == capacity, the oldest key (from front of queue) is removed.

2. TTL-Based Eviction
Each item has a ttl (in seconds).

The background thread runs periodically to remove items where:

python
Copy
Edit
item.ttl < current_timestamp
📊 Components Overview
🧠 LRUCache Class
Method	Description
put(key, value, ttl=100)	Insert/update a key with optional TTL
get(key)	Retrieve value if key exists and not expired
clear()	Clears all items from cache
get_stats()	Returns current stats as JSON
stop()	Stops TTL cleanup thread (call manually unless using with)

📈 Stats Class
Tracks:

hits, misses, hit_rate

total_requests, current_size

evictions, expired_removals

🪵 Logger Class
Logs events to a log.txt file via a static method:

python
Copy
Edit
Logger.log("your message here")
🧪 Sample Stats Output
Test	Output
Concurrent Access	{"hits": 500, "misses": 0, "hit_rate": 0.5, "total_requests": 1000, "current_size": 500, "evictions": 0, "expired_removals": 0}
Random Access	{"hits": 1, "misses": 0, "hit_rate": 0.5, "total_requests": 2, "current_size": 5, "evictions": 0, "expired_removals": 0}
Timestamp Expiry	{"hits": 0, "misses": 1, "hit_rate": 0.0, "total_requests": 1, "current_size": 3, "evictions": 0, "expired_removals": 1}

🧼 Cleanup Reminder
Always call stop() after use to cleanly shut down the TTL thread:

python
Copy
Edit
cache.stop()
OR use the with context block for auto-cleanup:

python
Copy
Edit
with LRUCache(4) as cache:
    ...
💡 Future Enhancements (Optional)
Switch to OrderedDict for simpler LRU management

TTL cleanup on-demand during get() calls

Fine-grained locking using read-write locks

Persistent storage for cache values