#!/usr/bin/env python3
"""
FIFOCache module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements a FIFOCache using the BaseCaching
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the FIFOCache
        """

        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())
            self.cache_data.pop(discard[0])
            print(f"DISCARD: {discard[0]}")

    def get(self, key):
        """
        Returns the value in cache_data linked to key
        """

        if key not in self.cache_data.keys() or key is None:
            return None

        return self.cache_data[key]
