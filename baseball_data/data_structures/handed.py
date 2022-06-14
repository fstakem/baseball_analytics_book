from __future__ import annotations
from enum import auto

from baseball_data.data_structures.auto_name import AutoName


class Handed(AutoName):
    LEFT = auto()
    RIGHT = auto()

    @classmethod
    def from_str(cls, value: str) -> Handed:
        new_value = value.lower()
        mapping = {'r': 'right', 'l': 'left'}

        return cls._from_str(new_value, mapping)
