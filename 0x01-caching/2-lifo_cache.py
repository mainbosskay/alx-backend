#!/usr/bin/env python3
"""Module for Last-In First-Out (LIFO) caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """Class object for storing and getting items using LIFO removal"""
    def __init__(self):
        """Initializing class for caching system"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adding an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lastKey, _ = self.cache_data.popitem(True)
                print("DISCARD:", lastKey)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Getting an item from cache using specific key"""
        return self.cache_data.get(key, None)
