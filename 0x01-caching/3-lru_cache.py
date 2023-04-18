#!/usr/bin/env python3
"""
LRUCache module
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Implements LRU Caching using base class BaseCaching
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the LRUCache
        """

        if key is None or item is None:
            pass

        else:
            self.cache_data[key] = item

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())

    def get(self, key):
        """
        Returns the value in cache_data linked to key
        """

        if key not in self.cache_data.keys() or key is None:
            return None

        return self.cache_data[key]
