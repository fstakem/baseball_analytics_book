from __future__ import annotations
from dataclasses import dataclass

from baseball_data.data_structures.league import League


@dataclass
class Team(object):
    abbreviation: str
    city: str
    name: str
    league: League
