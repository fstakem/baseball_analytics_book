from __future__ import annotations
from typing import Optional
from dataclasses import dataclass


@dataclass
class Count(object):
    balls: int
    strikes: int

    @classmethod
    def from_str(cls, value: str) -> Optional[Count]:
        if not value.isdigit():
            return None

        return Count(int(value[0]), int(value[1]))
