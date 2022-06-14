from __future__ import annotations
from enum import auto

from baseball_data.data_structures.auto_name import AutoName


class Base(AutoName):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()

    @classmethod
    def from_str(cls, value: str) -> Base:
        mapping = {'1': 'first', '2': 'second', '3': 'third'}

        return cls._from_str(value, mapping)
