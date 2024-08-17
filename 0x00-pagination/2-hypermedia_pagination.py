#!/usr/bin/env python3
"""Module for dataset of baby names of pagination"""
import csv
import math
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Getting and returns information about page for hypermedia"""
        dataPage = self.get_page(page, page_size)
        startIndx, endIndx = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        hyperMediaPageInfo = {
            "page_size": len(dataPage),
            "page": page,
            "data": dataPage,
            "next_page": page + 1 if endIndx < len(self.__dataset) else None,
            "prev_page": page - 1 if startIndx > 0 else None,
            "total_pages": total_pages
        }
        return hyperMediaPageInfo
