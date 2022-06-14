from __future__ import annotations
from enum import auto

from baseball_data.data_structures.auto_name import AutoName


class GameOfDay(AutoName):
    SINGLE = auto()
    FIRST_OF_DOUBLE_HEADER = auto()
    SECOND_OF_DOUBLE_HEADER = auto()

    @classmethod
    def from_str(cls, value: str) -> GameOfDay:
        new_value = int(value)
        mapping = {0: 'single', 1: 'first_of_double_header', 2: 'second_of_double_header'}

        return cls._from_str(new_value, mapping)
