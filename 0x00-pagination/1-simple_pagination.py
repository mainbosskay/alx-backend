#!/usr/bin/env python3
"""Module for dataset of baby names of pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Getting and returns index range for pagination for two int"""
    startIndx = (page - 1) * page_size
    endIndx = startIndx + page_size
    return (startIndx, endIndx)


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializing instance server"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset from csv file"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Getting and returns baby names specific page"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndx, endIndx = index_range(page, page_size)
        dataSets = self.dataset()
        if startIndx > len(dataSets):
            return []
        return dataSets[startIndx:endIndx]
