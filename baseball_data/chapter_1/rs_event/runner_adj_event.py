from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent
from baseball_data.data_structures.base import Base


@dataclass
class RunnerEvent(RsEvent):
    data_id: ClassVar[str] = 'radj'
    player_id: str
    base: Base
    
    @classmethod
    def from_tokens(cls, tokens: list[str]) -> RunnerEvent:
        return RunnerEvent(tokens[0], Base.from_str(tokens[1]))
