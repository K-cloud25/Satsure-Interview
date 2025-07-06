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


● Concurrency model


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

● Performance considerations