#!/usr/bin/env python3
"""
LFUCache module
"""


from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Implements LFU Caching using base class BaseCaching
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the LFUCache
        """

        if key is None or item is None:
            pass

        else:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())
            self.cache_data.pop(discard[-2])
            print(f"DISCARD: {discard[-2]}")

    def get(self, key):
        """
        Returns the value in cache_data linked to key
        """

        if key not in self.cache_data.keys() or key is None:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
