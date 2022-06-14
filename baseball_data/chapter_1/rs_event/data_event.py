from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent


@dataclass
class DataEvent(RsEvent):
    data_id: ClassVar[str] = 'data'
    player_id: str
    earned_runs: int
    
    @classmethod
    def from_tokens(cls, tokens: list[str]) -> DataEvent:
        return cls(player_id=tokens[1], earned_runs=int(tokens[2]))
