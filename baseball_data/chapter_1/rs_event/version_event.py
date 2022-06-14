from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent


@dataclass
class VersionEvent(RsEvent):
    data_id: ClassVar[str] = 'version'
    version: int
    
    @classmethod
    def from_tokens(cls, tokens: list[str]) -> VersionEvent:
        return cls(version=int(tokens[0]))
