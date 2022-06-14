from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent
from baseball_data.data_structures.handed import Handed


@dataclass
class BattingAdjEvent(RsEvent):
    data_id: ClassVar[str] = 'badj'
    player_id: str
    bat_side: Handed
    
    @classmethod
    def from_tokens(cls, tokens: list[str]) -> BattingAdjEvent:
        return cls(player_id=tokens[0], bat_side=Handed.from_str(tokens[1]))
