from __future__ import annotations
from typing import ClassVar
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent
from baseball_data.data_structures.team_side import TeamSide
from baseball_data.data_structures.fielding_position import FieldingPosition


@dataclass
class StartEvent(RsEvent):
    data_id: ClassVar[str] = 'start'
    player_id: str
    player_name: str
    team_side: TeamSide
    batting_order: int
    fielding_pos: FieldingPosition

    @classmethod
    def from_tokens(cls, tokens: list[str]) -> StartEvent:
        player_id = tokens[0]
        player_name = tokens[1].strip('"')
        team_side = TeamSide.from_str(tokens[2])
        batting_order = int(tokens[3])
        fielding_pos = FieldingPosition.from_str(tokens[4])

        return cls(player_id=player_id, player_name=player_name, team_side=team_side, batting_order=batting_order,
                   fielding_pos=fielding_pos)
