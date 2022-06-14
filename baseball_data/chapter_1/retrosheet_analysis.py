import json
import csv
from pathlib import Path

import pandas as pd

from baseball_data.chapter_1.rs_event.rs_event import RsEvent
from baseball_data.chapter_1.rs_event.rs_event_factory import RsEventFactory
from baseball_data.chapter_1.rs_event.id_event import IdEvent
from baseball_data.data_structures.game import Game


file_path = Path(__file__)
project_path = Path(__file__).parent.parent.parent.resolve()
data_path = project_path / 'data' / 'test_data'
retrosheet_path = data_path / 'retrosheet'
year = 2021
team = 'ATL'
teams = {'american': ['ANA', 'BAL', 'BOS', 'CHA', 'CLE', 'DET', 'HOU', 'KCA', 'MIN', 'NYA', 'OAK', 'SEA', 'TBA', 'TEX', 'TOR'],
         'national': ['ARI', 'ATL', 'CHN', 'CIN', 'COL', 'LAN', 'MIA', 'MIL', 'NYN', 'PHI', 'PIT', 'SDN', 'SFN', 'SLN', 'WAS']}
file_ending = {'american': 'EVA', 'national': 'EVN'}


def get_config(path: Path) -> dict:
    with open(file_path.parent / 'retrosheet_config.json') as f:
        return json.load(f)


def get_gamelog(retrosheet_path: Path, year: int, config: dict) -> pd.DataFrame:
    path = retrosheet_path / 'gamelog' / f'GL{year}.TXT'
    df = pd.read_csv(path, header=None, names=config['gamelog']['col_names'])
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

    return df


def get_play_by_play(retrosheet_path: Path, year: int, league: str, team: str, config: dict) -> list[RsEvent]:
    end = file_ending[league]
    path = retrosheet_path / 'play_by_play' / f'{year}{team}.{end}'
    output: list = []
    factory = RsEventFactory()

    with open(path, 'r') as f:
        lines = f.readlines()

        for i, tokens in enumerate(csv.reader(lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True)):
            try:
                output.append(factory.from_tokens(tokens))
            
            except Exception as e:
                print(i, e)
                print(f'ERROR: {tokens}')

    return output


def get_games(retrosheet_path: Path, year: int, league: str, team: str, config: dict):
    pbp_events = get_play_by_play(retrosheet_path, year, league, team, config)
    games = []
    game = Game()

    for i, e in enumerate(pbp_events):
        if type(e) is IdEvent:
            if game.has_events():
                games.append(game.populate())

            game = Game(events=[e])

        else:
            game.events.append(e)

    games.append(game.populate())

    return games


def get_all_games(retrosheet_path: Path, year: int, config: dict):
    games = []

    for league, league_teams in teams.items():
        for t in league_teams:
            games.extend(get_games(retrosheet_path, year, league, t, config))

    return games
       

def get_roster(retrosheet_path: Path, year: int, team: str, ) -> pd.DataFrame:
    path = retrosheet_path / 'play_by_play' / f'{team}{year}.ROS'
    df = pd.read_csv(path, header=None, names=['abbreviation', 'last_name', 'first_name', 'bat_side', 'throw_side', 'team', 'pos'])

    return df


def get_teams(retrosheet_path: Path, year: int) -> pd.DataFrame:
    path = retrosheet_path / 'play_by_play' / f'TEAM{year}'
    df = pd.read_csv(path, header=None, names=['abbreviation', 'league', 'city', 'team'])

    return df


config = get_config(file_path)
gamelog_df = get_gamelog(retrosheet_path, year, config)
games = get_all_games(retrosheet_path, year, config)
braves_games = [g for g in games if g.home == 'ATL' or g.visitor == 'ATL']
roster_dfs = [get_roster(retrosheet_path, year, t) for _, league_teams in teams.items() for t in league_teams]
roster_df = pd.concat(roster_dfs)
team_df = get_teams(retrosheet_path, year)

import ipdb
ipdb.set_trace()
