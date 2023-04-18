#!/usr/bin/env python3
"""
BasicCache module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Implements a caching system using the BaseCaching class
    """

    def put(self, key, item):
        """
        Assign an item to the cache_data dictionary using
        the key
        """

        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in cache_data linked to key
        """

        if key not in self.cache_data.keys() or key is None:
            return None

        return self.cache_data[key]
