import time
from collections import deque
from threading import Lock, Thread, Event
from datetime import datetime
from models.CacheItem import CacheItem
from models.Logger import Logger
from models.Stats import Stats
from collections import deque

class LRUCache:

    def __init__(self, capacity):
        Logger.log("init")
        self.stat = Stats()
        
        # Data Vars
        self.map = dict()
        self.capacity = capacity
        self.queue = deque()
        
        # Threading Vars
        self.lock = Lock()
        self.flag = Event()
        self.thread = Thread(target=self.clearByTimestamp)
        self.thread.daemon = True
        self.thread.start()
        
    def __enter__(self):
        Logger.log("Context Based Init")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if ( exc_type ):
            Logger.log(str(exc_val),"Error")
        Logger.log("Ending Stats : " + self.stat.get_stats())
        self.stop()

    def get(self, key) -> str:
        self.stat.updateRequest()
        with self.lock:
            if key not in self.map:
                self.stat.updateMiss()
                return "-1"
            else:
                self.stat.updateHits()
                try:
                    self.queue.remove(key)
                except ValueError:
                    Logger.log("Invalid Key Enterd = " + key)
                    pass
                
                self.queue.append(key)
                return self.map[key].getValue()

    def put(self, key, value, ttl=100):
        with self.lock:
            if key in self.map:
                try:
                    self.queue.remove(key)
                except ValueError:
                    Logger.log("Invalid Key Removal" + key)
                    pass
            elif len(self.map) == self.capacity:
                self.stat.updateEviction()
                oldest = self.queue.popleft()
                del self.map[oldest]
                
            cacheItem = CacheItem(key, value, ttl)
            self.map[key] = cacheItem
            self.queue.append(key)
        self.stat.updateSize(self.capacity)

    def clearByTimestamp(self) -> None:
        Logger.log("TTL check thread started")
        while not self.flag.is_set():
            with self.lock:
                current_ts = int(datetime.now().timestamp())
                keys_to_remove = [key for key, item in self.map.items() if item.ttl < current_ts]
                for key in keys_to_remove:
                    try:
                        self.queue.remove(key)
                    except ValueError:
                        pass
                    del self.map[key]
                self.stat.updateExpired(len(keys_to_remove))
                Logger.log("Clear Keys : " + str(keys_to_remove))
            time.sleep(10) 

    def clear(self):
        self.stat.updateSize(0)
        with self.lock:
            self.capacity = 0;
            self.map.clear()
            self.queue.clear()
        
    def stop(self):
        Logger.log("cache destroyed")
        self.flag.set()
        self.thread.join()    
    
    def get_stats(self) ->str:
        return self.stat.get_stats()