import json
class Stats:
    
    def __init__(self) -> None:
        self.hits=0
        self.hit_rate=0
        self.misses=0
        self.total_requests=0
        self.current_size=0
        self.evictions=0
        self.expired_removals=0
    
    def updateHits(self, delta:int =1) -> None:
        self.hits += delta
    def updateMiss(self, delta:int =1) -> None:
        self.misses += delta
    def updateRequest(self, delta:int =1) -> None:
        self.total_requests += delta
    def updateSize(self, size) -> None:
        self.current_size = size
    def updateEviction(self, delta:int =1) -> None:
        self.evictions += delta        
    def updateExpired(self, delta:int =1) -> None:
        self.expired_removals += delta
        
        
    def get_stats(self) -> str:
        if self.total_requests > 0:
            self.hit_rate = round(self.hits / self.total_requests, 3)
        else:
            self.hit_rate = 0.0

        return json.dumps({
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": self.hit_rate,
            "total_requests": self.total_requests,
            "current_size": self.current_size,
            "evictions": self.evictions,
            "expired_removals": self.expired_removals
        })