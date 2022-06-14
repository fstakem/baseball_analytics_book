from __future__ import annotations
from dataclasses import dataclass, field
# from typing import TypeVar

# from baseball_data.chapter_1.rs_event.rs_event import RsEvent
from baseball_data.chapter_1.rs_event.info_event import InfoEvent

# T = TypeVar('T', bound=RsEvent)


@dataclass
class Game(object):
    events: list = field(default_factory=lambda: [])
    home: str = ''
    visitor: str = ''

    def has_events(self) -> bool:
        if len(self.events):
            return True

        return False

    def populate(self) -> Game:
        for e in self.events:
            if type(e) is InfoEvent:
                if 'hometeam' in e.data:
                    self.home = e.data['hometeam']

                elif 'visteam' in e.data:
                    self.visitor = e.data['visteam']

        return self
    