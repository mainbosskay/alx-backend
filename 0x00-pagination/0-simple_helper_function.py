#!/usr/bin/env python3
"""Module for index_range function of pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Getting and returns index range for pagination for two int"""
    startIndx = (page - 1) * page_size
    endIndx = startIndx + page_size
    return (startIndx, endIndx)
