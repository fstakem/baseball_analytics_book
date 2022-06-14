from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent


@dataclass
class OrderAdjEvent(RsEvent):
    data_id: ClassVar[str] = 'ladj'
    
    @classmethod
    def from_tokens(cls, tokens: list[str]) -> OrderAdjEvent:
        raise NotImplementedError('Need order ajustment event implemented')
