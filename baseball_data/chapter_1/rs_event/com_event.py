from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent


@dataclass
class ComEvent(RsEvent):
    data_id: ClassVar[str] = 'com'
    msg: str
    
    @classmethod
    def from_tokens(cls, tokens: list[str]) -> ComEvent:
        return cls(msg=tokens[0].strip('"'))
