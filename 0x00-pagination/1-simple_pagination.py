#!/usr/bin/env python3
"""Module to paginate items from a dataset of popular baby names."""
import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> tuple:
        """Calculate the start and end indexes for the pagination parameters"""
        start = (page - 1) * page_size
        end = page * page_size
        return start, end

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of items from the dataset."""
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        start, end = self.index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start:end]
