from __future__ import annotations
from enum import auto

from baseball_data.data_structures.auto_name import AutoName


class FieldingPosition(AutoName):
    PITCHER = auto()
    CATCHER = auto()
    FIRST_BASE = auto()
    SECOND_BASE = auto()
    THIRD_BASE = auto()
    SHORT_STOP = auto()
    LEFT_FIELD = auto()
    CENTER_FIELD = auto()
    RIGHT_FIELD = auto()
    DH = auto()
    PINCH_HITTER = auto()
    PINCH_RUNNER = auto()

    @classmethod
    def from_str(cls, value: str) -> FieldingPosition:
        new_value = int(value)
        mapping = {1: 'pitcher', 2: 'catcher', 3: 'first_base', 4: 'second_base', 5: 'third_base', 6: 'short_stop',
                   7: 'left_field', 8: 'center_field', 9: 'right_field', 10: 'dh', 11: 'pinch_hitter',
                   12: 'pinch_runner'}

        return cls._from_str(new_value, mapping)
