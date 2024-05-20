#!/usr/bin/env python3
"""Simple helper function to calculate start and end index for pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
