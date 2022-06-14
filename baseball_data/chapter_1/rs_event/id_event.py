from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass
from datetime import date


from baseball_data.chapter_1.rs_event.rs_event import RsEvent
from baseball_data.data_structures.game_of_day import GameOfDay


@dataclass
class IdEvent(RsEvent):
    data_id: ClassVar[str] = 'id'
    home_team: str
    date: date
    game: GameOfDay

    @classmethod
    def from_tokens(cls, tokens: list[str]) -> IdEvent:
        team = tokens[0][:3]
        day = int(tokens[0][9:11])
        month = int(tokens[0][7:9])
        year = int(tokens[0][3:7])
        game = GameOfDay.from_str(tokens[0][-1])
        game_date = date(year, month, day)

        return cls(home_team=team, date=game_date, game=game)
