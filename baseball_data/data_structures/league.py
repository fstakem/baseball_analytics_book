from __future__ import annotations
from enum import auto

from baseball_data.data_structures.auto_name import AutoName


class League(AutoName):
    AMERICAN = auto()
    NATIONAL = auto()

    @classmethod
    def from_str(cls, value: str) -> League:
        mapping = {'A': 'american', 'N': 'national'}

        return cls._from_str(value, mapping)
