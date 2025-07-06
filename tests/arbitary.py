from models.LRUCache import LRUCache
import unittest
import time

class TestStringMethods(unittest.TestCase):

    def test(self):
        with LRUCache(5) as cache:
            cache.put("key1", "val1")            
            self.assertEqual(cache.get("key1"), "val1")
    
    def test2(self):
        with LRUCache(3) as cache:
            cache.put("key1", "val1")
            cache.put("key2", "val2")
            
            cache.get("key1")
            
            cache.put("key3", "val3")
            cache.put("key4", "val4")
            
            self.assertEqual(cache.get("key2"), "-1")
            
    def test3(self):
        with LRUCache(3) as cache:
            cache.put("key1", "val1", 1)
            time.sleep(10)   # loop time of thread
            self.assertEqual(cache.get("key1"), "-1")

if __name__ == '__main__':
    unittest.main()