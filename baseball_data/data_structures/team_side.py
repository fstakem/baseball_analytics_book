from __future__ import annotations
from enum import auto

from baseball_data.data_structures.auto_name import AutoName


class TeamSide(AutoName):
    HOME = auto()
    VISITOR = auto()

    @classmethod
    def from_str(cls, value: str) -> TeamSide:
        new_value = int(value)
        mapping = {0: 'visitor', 1: 'home'}

        return cls._from_str(new_value, mapping)
