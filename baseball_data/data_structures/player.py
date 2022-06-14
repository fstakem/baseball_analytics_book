from __future__ import annotations
from dataclasses import dataclass

from baseball_data.data_structures.player_side import PlayerSide
from baseball_data.data_structures.fielding_position import FieldingPosition


@dataclass
class Player(object):
    player_id: str
    first_name: str
    last_name: str
    bat_side: PlayerSide
    throw_side: PlayerSide
    team_abbrv: str
    pos: FieldingPosition
