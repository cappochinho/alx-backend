#!/usr/bin/env python3

"""
Module for simple pagination'
"""

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page: int -> page to start from
        page_size: int -> the size of the page

    This function returns a tuple of size two containing
    a start index and an end index corresponding to the range
    of indexes to return in a list for those particular
    pagination parameters
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        try:
            data = self.dataset()
            start_idx, end_idx = index_range(page, page_size)
            return data[start_idx: end_idx]

        except (EOFError):
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary that contains following metadata
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)

        if start_idx >= len(dataset):
            return {
                "page_size": 0,
                "page": page,
                "data": [],
                "next_page": None,
                "prev_page": None,
                "total_pages": 0
            }

        next_page = page + 1 if end_idx < len(dataset) else None

        prev_page = page - 1 if start_idx > 0 else None

        data = dataset[start_idx:end_idx]
        page_size = len(data)
        total_pages = math.ceil(len(dataset) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
