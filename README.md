● How to run the code (with commands for setup and execution)
    1. CMD to run test
        `python -m unittest tests/concurr`
        `python -m unittest tests/arbitart`
    2. To run Cache for other cases
        1. Object Instantiate Method
            1. Import LRUCache from models
            2. Object should be instantaite with max size for cache
            3. method:  
                obj.put(key:str, value:str, ttl=100)
                obj.get(key:str) -> str
                obj.clear()
                obj.get_stats()->str
            4. Post use *PLEASE* use the stop function for clean up 
                obj.stop()

        2. Context Based Instantation Method
            1. Import LRUCache from models
            2. cache object can be used with context based method
                `with LRUCache(4) as cache:`
            3. In this case no requirement to call stop function as it is called implicity after code block exit        

● Dependencies
    1. python version 3.13.1

● Design decisions
    1. Data structure
    To manage the LRU Cache the below data structure are utilized
        1. Queue : The queue structure of nodes help check which key was used the latest. The key at the end of the queue is the key that was not used recently. This helps with the elimination of the key from the cache.
        2. Map: The map is used to access keys with O(1) time complexity. This help manage the access logic of the cache
    
    2. LRU Cache:
        1. The class uses Thread lock and event to manage the concurrent use of the global variables and inter thread communication.
        2. The Constructor method of the class starts a thread that periodically checks the timetamps of the keys in cache and removes the expired keys.
        3. The clean up function makes sure that the daemon thread is joined to ensure proper thread management
        4. The class also implements the LRU logic to handle the requirement of the cache.
    
    3. Stats class:
        1. Simple class to store the statsitics requirement of the question and return the report when requested.
    
    4. Logger class:
        1. Implements a simple static function to write to a log.txt file

● Concurrency model
    Global locks are implmented to restrict use of resources like queue and map.
    The Lock ensures code that code is thread safe.

● Eviction logic

1. Due to Size
    1. If the max size of LRUCache is about to exceed
    2. The older key from the queue is popped and removed from the cache
    3. The `dequeue` helps manage the latest key accessed and map help with O(1) access of keys

2. Due to expired TTL
    1. By Default each key is given a TTL of 100 seconds
    2. The TTL is set according to current timestamp + given ttl
    3. The background daemon thread check the list of current keys and compares the timestamp with the current timestamp value
    4. A sublist of keys is created from total list of keys which pass eviction condition of `if item.ttl < current_ts` 

● Sample stats output 
    Concur Test: {"hits": 500, "misses": 0, "hit_rate": 0.5, "total_requests": 1000, "current_size": 500, "evictions": 0, "expired_removals": 0}

    Random Test : {"hits": 1, "misses": 0, "hit_rate": 0.5, "total_requests": 2, "current_size": 5, "evictions": 0, "expired_removals": 0}

    Timestamp test : {"hits": 0, "misses": 1, "hit_rate": 0.0, "total_requests": 1, "current_size": 3, "evictions": 0, "expired_removals": 1}
