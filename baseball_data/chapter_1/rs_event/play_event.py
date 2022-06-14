from __future__ import annotations
from typing import ClassVar, Optional
from dataclasses import dataclass

from baseball_data.chapter_1.rs_event.rs_event import RsEvent
from baseball_data.data_structures.team_side import TeamSide
from baseball_data.data_structures.count import Count
from baseball_data.data_structures.pitch import Pitch


@dataclass
class PlayEvent(RsEvent):
    data_id: ClassVar[str] = 'play'
    inning: int
    team_side: TeamSide
    player_id: str
    count: Optional[Count]
    pitches: list[Pitch]
    desc: str  # This field is complex and needs to be broken up more

    # Parse the desc field
    # 1 description
    # 2 / modifier
    # 3 runner advance
    
    @classmethod
    def from_tokens(cls, tokens: list[str]) -> PlayEvent:
        inning = int(tokens[0])
        team_side = TeamSide.from_str(tokens[1])
        player_id = tokens[2]
        count = Count.from_str(tokens[3])
        pitches = [Pitch.from_str(x) for x in tokens[4]]
        desc = tokens[5]

        return PlayEvent(inning=inning, team_side=team_side, player_id=player_id, count=count, pitches=pitches,
                         desc=desc)
