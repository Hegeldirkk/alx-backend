#!/usr/bin/env python3
"""simple helper"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """pagination"""
    a = (page - 1) * page_size
    b = page * page_size
    return (a, b)
