from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent


@dataclass
class InfoEvent(RsEvent):
    data_id: ClassVar[str] = 'info'
    data: dict
    
    @classmethod
    def from_tokens(cls, tokens: list[str]) -> InfoEvent:
        data = {}

        for i in range(0, len(tokens), 2):
            data[tokens[i]] = tokens[i + 1]

        return cls(data=data)
