# 🧠 LRUCache — Thread-Safe Cache with TTL Support

A thread-safe, TTL-enabled Least Recently Used (LRU) cache implementation in Python. Designed for concurrent workloads, it supports both object-oriented and context-managed usage.

---

## 🚀 How to Run the Code

### 💡 Run Unit Tests

```bash
python -m unittest tests/concurr
python -m unittest tests/arbitart
```

### 🔧 Using the LRUCache

#### 1. Object-Based Usage

```python
from models.LRUCache import LRUCache

cache = LRUCache(max_size=4)

cache.put("key1", "value1", ttl=60)
print(cache.get("key1"))
print(cache.get_stats())
cache.clear()
cache.stop()  # Important for cleanup
```

#### 2. Context-Based Usage

```python
from models.LRUCache import LRUCache

with LRUCache(max_size=4) as cache:
    cache.put("key2", "value2")
    print(cache.get("key2"))
# `stop()` is automatically called on exit
```

---

## 📦 Dependencies

* Python **3.13.1**
* No third-party libraries required

---

## ⚙️ Design Overview

### 📖 Data Structures

| Structure | Purpose                            |
| --------- | ---------------------------------- |
| `deque`   | Maintains access order (LRU logic) |
| `dict`    | Provides O(1) key-value access     |

### 🤜 Concurrency Model

* Global `threading.Lock` ensures safe access to shared structures
* Background daemon thread handles TTL-based cleanup
* Graceful shutdown via `stop()` or context manager

### ♻️ Eviction Logic

#### 1. Size-Based

* When max size is reached, the oldest key is evicted (front of the queue)

#### 2. TTL-Based

* Keys expire after `ttl` seconds
* Background thread removes expired entries every second

---

## 📊 Components

### 🔬 LRUCache API

| Method                     | Description                                     |
| -------------------------- | ----------------------------------------------- |
| `put(key, value, ttl=100)` | Inserts or updates a key with optional TTL      |
| `get(key)`                 | Retrieves value if key exists and isn't expired |
| `clear()`                  | Clears the cache                                |
| `get_stats()`              | Returns a JSON string of stats                  |
| `stop()`                   | Terminates the TTL cleanup thread               |

### 📉 Stats Class

Tracks:

* Hits / Misses
* Hit rate
* Total requests
* Current size
* Evictions / Expired removals

### 📝 Logger Class

Logs messages to `log.txt`:

```python
Logger.log("your message")
```

---

## 📊 Sample Stats Output

| Test Case         | Output                                                                                                                              |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Concurrent Access | `{ "hits": 500, "misses": 0, "hit_rate": 0.5, "total_requests": 1000, "current_size": 500, "evictions": 0, "expired_removals": 0 }` |
| Random Access     | `{ "hits": 1, "misses": 0, "hit_rate": 0.5, "total_requests": 2, "current_size": 5, "evictions": 0, "expired_removals": 0 }`        |
| Timestamp Expiry  | `{ "hits": 0, "misses": 1, "hit_rate": 0.0, "total_requests": 1, "current_size": 3, "evictions": 0, "expired_removals": 1 }`        |

---

## 🚨 Cleanup Reminder

Always call `stop()` to terminate the TTL thread if not using a `with` block.

```python
cache.stop()
```

---

## 💡 Future Enhancements

* Use `OrderedDict` for simplified LRU logic
* TTL eviction on-demand during `get()`
* Read-write lock support for more parallelism
* Persistent caching support

---

## 🌐 License

MIT License. Use freely, but don't forget to credit if reused in production systems!
