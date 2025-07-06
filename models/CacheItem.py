import time
from datetime import datetime
class CacheItem:    
    def __init__(self, key, value, ttl:int=1000):
        self.key = key
        self.value = value
        self.ttl = ttl + int ( datetime.now().timestamp() )
    
    def getValue(self) -> str:
        return self.value
        
        
        