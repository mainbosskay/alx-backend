#!/usr/bin/env python3
"""Module for Least Frequently Used caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """Class object for storing and getting items using LFU removal"""
    def __init__(self):
        """Initializing class for caching system"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.trackFreq = []

    def freqUpdate(self, mruKey):
        """Updating cache items based on the most recently used"""
        maxPos = []
        freqMru = 0
        posMru = 0
        posInserted = 0
        for indx, freqTrack in enumerate(self.trackFreq):
            if freqTrack[0] == mruKey:
                freqMru = freqTrack[1] + 1
                posMru = indx
                break
            elif len(maxPos) == 0:
                maxPos.append(indx)
            elif freqTrack[1] < self.trackFreq[maxPos[-1]][1]:
                maxPos.append(indx)
        maxPos.reverse()
        for pos in maxPos:
            if self.trackFreq[pos][1] > freqMru:
                break
            posInserted = pos
        self.trackFreq.pop(posMru)
        self.trackFreq.insert(posInserted, [mruKey, freqMru])

    def put(self, key, item):
        """Adding an item in the cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfuKey, _ = self.trackFreq[-1]
                self.cache_data.pop(lfuKey)
                self.trackFreq.pop()
                print("DISCARD:", lfuKey)
            self.cache_data[key] = item
            indxInserted = len(self.trackFreq)
            for indx, freqTrack in enumerate(self.trackFreq):
                if freqTrack[1] == 0:
                    indxInserted = indx
                    break
            self.trackFreq.insert(indxInserted, [key, 0])
        else:
            self.cache_data[key] = item
            self.freqUpdate(key)

    def get(self, key):
        """Getting an item from cache using specific key"""
        if key is not None and key in self.cache_data:
            self.freqUpdate(key)
        return self.cache_data.get(key, None)
