#!/usr/bin/env python3
"""Module for First-In First-Out (FIFO) caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Class object for storing and getting items using FIFO removal"""
    def __init__(self):
        """Initializing class for caching system"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adding an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstKey, _ = self.cache_data.popitem(False)
            print("DISCARD:", firstKey)

    def get(self, key):
        """Getting an item from cache using specific key"""
        return self.cache_data.get(key, None)
