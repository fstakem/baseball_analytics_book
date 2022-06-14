from pathlib import Path

import pandas as pd

project_path = Path(__file__).parent.parent.parent.resolve()
data_path = project_path / 'data' / 'test_data'
lahman_path = data_path / 'lahman' / 'baseballdatabank-2022.2'


def get_people(lahman_path: Path) -> pd.DataFrame:
    people_path = lahman_path / 'core' / 'People.csv'
    people_df = pd.read_csv(people_path)
    int_fields = ['birthYear', 'birthMonth', 'birthDay']
    people_df[int_fields] = people_df[int_fields].fillna(0).astype(int)

    return people_df


def get_batting(lahman_path: Path) -> pd.DataFrame:
    batting_path = lahman_path / 'core' / 'Batting.csv'
    batting_df = pd.read_csv(batting_path)

    return batting_df


def get_pitching(lahman_path: Path) -> pd.DataFrame:
    pitching_path = lahman_path / 'core' / 'Pitching.csv'
    pitching_df = pd.read_csv(pitching_path)

    return pitching_df


def get_fielding(lahman_path: Path) -> pd.DataFrame:
    fielding_path = lahman_path / 'core' / 'Fielding.csv'
    fielding_df = pd.read_csv(fielding_path)
    int_fields = ['GS', 'InnOuts', 'E']
    fielding_df[int_fields] = fielding_df[int_fields].fillna(0).astype(int)

    return fielding_df


def get_teams(lahman_path: Path) -> pd.DataFrame:
    teams_path = lahman_path / 'core' / 'Teams.csv'
    teams_df = pd.read_csv(teams_path)
    int_fields = ['Ghome', 'BB', 'SO', 'SB', 'HBP', 'attendance']
    teams_df[int_fields] = teams_df[int_fields].fillna(0).astype(int)

    return teams_df


people_df = get_people(lahman_path)
batting_df = get_batting(lahman_path)
pitching_df = get_pitching(lahman_path)
fielding_df = get_fielding(lahman_path)
teams_df = get_teams(lahman_path)

import ipdb
ipdb.set_trace()