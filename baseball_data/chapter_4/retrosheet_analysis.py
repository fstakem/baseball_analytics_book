import json
from pathlib import Path

import pandas as pd
from pandas.core.series import Series
from skimpy import skim
import matplotlib.pyplot as plt

file_path = Path(__file__)
project_path = Path(__file__).parent.parent.parent.resolve()
data_path = project_path / 'data' / 'test_data'
retrosheet_path = data_path / 'retrosheet'
data_path = project_path / 'data' / 'test_data'
lahman_path = data_path / 'lahman' / 'baseballdatabank-2021.2'
wpct_path = project_path / 'baseball_data' / 'chapter_4' / 'lahman_wpct.csv'


def get_config(path: Path) -> dict:
    with open(file_path.parent / 'retrosheet_config.json') as f:
        return json.load(f)


def get_gamelog(retrosheet_path: Path, year: int, config: dict) -> pd.DataFrame:
    path = retrosheet_path / 'gamelog' / f'GL{year}.TXT'
    df = pd.read_csv(path, header=None, names=config['gamelog']['col_names'])
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

    return df


def get_pitching(lahman_path: Path) -> pd.DataFrame:
    pitching_path = lahman_path / 'core' / 'Pitching.csv'
    pitching_df = pd.read_csv(pitching_path)

    return pitching_df


def score_diff(team: str):
    team = team

    def func(row: Series):
        if row.h_team == team:
            return row.h_team_score - row.v_team_score

        return row.v_team_score - row.h_team_score

    return func


def win_or_loss(row: Series) -> str:
    if row.score_diff > 0:
        return 'w'

    return 'l' 


def losing_team(team: str):
    team = team

    def func(row: Series) -> str:
        if row.h_team == team:
            return row.v_team

        return row.h_team

    return func


def score_diff_all(row: Series):
    if row.h_team_score > row.v_team_score:
        return row.h_team_score - row.v_team_score

    return row.v_team_score - row.h_team_score


def winning_team_all(row: Series):
    if row.h_team_score > row.v_team_score:
        return row.h_team

    return row.v_team


def plot_residuals_vs_one_run_count(x, y, labels) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y)
    ax.set_xlabel("One Run Wins")
    ax.set_ylabel("Pythagorean Residuals")

    for i, txt in enumerate(labels):
        ax.annotate(txt, (x[i], y[i]))
    

year = 2021
team = 'ATL'
config = get_config(file_path)
gamelog_df = get_gamelog(retrosheet_path, year, config)

# Atlanta
team_gamelog_df = gamelog_df[(gamelog_df['h_team'] == team) | (gamelog_df['v_team'] == team)]
df = team_gamelog_df[['h_team', 'v_team', 'h_team_score', 'v_team_score']]
df['score_diff'] = df.apply(score_diff(team), axis=1)
df['outcome'] = df.apply(win_or_loss, axis=1)

df.groupby('outcome')['score_diff'].describe()

one_run_df = df[df['score_diff'] == 1]
one_run_df['loser'] = df.apply(losing_team(team), axis=1)

wpct_df = pd.read_csv(wpct_path, index_col=0)
fwpct_df = wpct_df[(wpct_df['yearID'] == year)]
fwpct_df.replace(to_replace={'LAA': 'ANA'}, inplace=True)

total_df = pd.merge(one_run_df, fwpct_df, left_on='loser', right_on='teamID', how='inner')


# All teams
all_df = gamelog_df[['h_team', 'v_team', 'h_team_score', 'v_team_score']]
all_df['score_diff'] = all_df.apply(score_diff_all, axis=1)
all_df['winner'] = all_df.apply(winning_team_all, axis=1)

all_one_run_df = all_df[all_df['score_diff'] == 1]

team_one_run_wins_df = all_one_run_df.groupby('winner').size().reset_index(name='counts')
all_total_df = pd.merge(team_one_run_wins_df, fwpct_df, left_on='winner', right_on='teamID', how='inner')

plot_residuals_vs_one_run_count(all_total_df['counts'], all_total_df['residuals'], all_total_df['winner'])
# plt.show()

# Pitching
pitching_df = get_pitching(lahman_path)
good_pitching_df = pitching_df[(pitching_df['GF'] > 50) & (pitching_df['ERA'] < 2.5)]
pitch_df = good_pitching_df[['playerID', 'yearID', 'teamID']]

# Runs for a win

import ipdb
ipdb.set_trace()