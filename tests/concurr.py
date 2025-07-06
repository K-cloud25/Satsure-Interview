import threading
import unittest
from models.LRUCache import LRUCache  # replace with actual module path

class TestLRUCacheConcurrentAccess(unittest.TestCase):
    def test_concurrent_put(self):
        cache_capacity = 500
        cache = LRUCache(cache_capacity)

        def worker(thread_id):
            for i in range(100):
                cache.put(f"thread_{thread_id}:item_{i}", f"data_{i}")
                cache.get(f"thread_{thread_id}:item_{i//2}")

        threads = []
        for t_id in range(5):  # 5 threads inserting 100 items each
            t = threading.Thread(target=worker, args=(t_id,))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        # Validation
        total_items = len(cache.map)
        self.assertLessEqual(total_items, cache_capacity, "Cache exceeds capacity")
        print(cache.get_stats())
        cache.stop()

if __name__ == "__main__":
    unittest.main()