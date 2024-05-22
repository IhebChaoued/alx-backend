#!/usr/bin/env python3
""" LIFO caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system with LIFO eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.last_key]
            print(f"DISCARD: {self.last_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None:
            return None
        return self.cache_data.get(key)
