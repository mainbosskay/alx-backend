#!/usr/bin/env python3
"""Module for Most Recently Used caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Class object for storing and getting items using MRU removal"""
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
                mruKey, _ = self.cache_data.popitem(False)
                print("DISCARD:", mruKey)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Getting an item from cache using specific key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
