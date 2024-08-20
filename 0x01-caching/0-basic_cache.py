#!/usr/bin/env python3
"""Module for implementing basic caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class that represents an object for item storage and retrieval"""
    def __init__(self):
        """Initializing system class for caching"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Adding an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Getting an item from the cache using specific key"""
        return self.cache_data.get(key, None)
