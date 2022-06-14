from __future__ import annotations
from enum import auto

from baseball_data.data_structures.auto_name import AutoName


class Pitch(AutoName):
    BALL = auto()
    CALLED_STRIKE = auto()
    FOUL = auto()
    HIT_BATTER = auto()
    INTENTIONAL_BALL = auto()
    STRIKE = auto()
    FOUL_BUNT = auto()
    MISSED_BUNT = auto()
    NO_PITCH = auto()
    FOUL_TIP_ON_BUNT = auto()
    PITCHOUT = auto()
    SWING_ON_PITCHOUT = auto()
    FOUL_ON_PITCHOUT = auto()
    SWINGING_STRIKE = auto()
    FOUL_TIP = auto()
    UNKNOWN_OR_MISSED_PITCH = auto()
    BALL_ON_PITCHER_TO_MOUTH = auto()
    BALL_PUT_IN_PLAY_BY_BATTER = auto()
    BALL_PUT_IN_PLAY_ON_PITCHOUT = auto()
    FOLLOWING_CATCHER_PICKOFF_THROW = auto()
    PITCH_BLOCKED_BY_CATCHER = auto()
    PLAY_NOT_INVOLVING_BATTER = auto()
    PICKOFF_TO_FIRST = auto()
    PICKOFF_TO_SECOND = auto()
    PICKOFF_TO_THIRD = auto()
    RUNNER_GOING_ON_PITCH = auto()

    @classmethod
    def from_str(cls, value: str) -> Pitch:
        mapping = {'B': 'ball', 'C': 'called_strike', 'F': 'foul', 'H': 'hit_batter', 'I': 'intentional_ball',
                   'K': 'strike', 'L': 'foul_bunt', 'M': 'missed_bunt', 'N': 'no_pitch', 'O': 'foul_tip_on_bunt',
                   'P': 'pitchout', 'Q': 'swing_on_pitchout', 'R': 'foul_on_pitchout', 'S': 'swinging_strike',
                   'T': 'foul_tip', 'U': 'unknown_or_missed_pitch', 'V': 'ball_on_pitcher_to_mouth',
                   'X': 'ball_put_in_play_by_batter', 'Y': 'ball_put_in_play_on_pitchout', 
                   '+': 'following_catcher_pickoff_throw', '*': 'pitch_blocked_by_catcher',
                   '.': 'play_not_involving_batter', '1': 'pickoff_to_first', '2': 'pickoff_to_second',
                   '3': 'pickoff_to_third', '>': 'runner_going_on_pitch'}

        return cls._from_str(value, mapping)
