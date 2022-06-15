from pathlib import Path

import pandas as pd
from pandas.core.series import Series

file_path = Path(__file__).parent
project_path = Path(__file__).parent.parent.parent.resolve()
all_data_path = file_path / 'all2016.csv'
fields_path = file_path / 'fields.csv'


def str_to_value(row: str) -> str:
    if len(row) > 0:
        return '1'

    return '0'


def first_occupied_after_play(row: Series) -> int:
    if row['RUN1_DEST_ID'] == 1 | row['BAT_DEST_ID'] == 1:
        return 1

    return 0


def second_occupied_after_play(row: Series) -> int:
    if row['RUN1_DEST_ID'] == 2 | row['RUN2_DEST_ID'] == 2 | row['BAT_DEST_ID'] == 2:
        return 1

    return 0


def third_occupied_after_play(row: Series) -> int:
    if row['RUN1_DEST_ID'] == 3 | row['RUN2_DEST_ID'] == 3 | row['RUN3_DEST_ID'] == 3 | row['BAT_DEST_ID'] == 3:
        return 1

    return 0


fields_df = pd.read_csv(fields_path)
headers = fields_df['Header']
all_data_df = pd.read_csv(all_data_path, header=None, names=headers)
all_data_df.fillna('', inplace=True)
all_data_df['RUNS'] = all_data_df['AWAY_SCORE_CT'] + all_data_df['HOME_SCORE_CT']
all_data_df['HALF_INNING'] = all_data_df['GAME_ID'].astype(str) + all_data_df['INN_CT'].astype(str) + all_data_df['BAT_HOME_ID'].astype(str)
all_data_df['RUNS_SCORED'] = (all_data_df['BAT_DEST_ID'] > 3).astype(int) + \
                             (all_data_df['RUN1_DEST_ID'] > 3).astype(int) + \
                             (all_data_df['RUN2_DEST_ID'] > 3).astype(int) + \
                             (all_data_df['RUN3_DEST_ID'] > 3).astype(int)
all_data_df['OUTS_INNINGS'] = all_data_df.groupby('HALF_INNING')['EVENT_OUTS_CT'].transform('sum')
all_data_df['RUNS_INNINGS'] = all_data_df.groupby('HALF_INNING')['RUNS_SCORED'].transform('sum')
all_data_df['RUNS_START'] = all_data_df.groupby('HALF_INNING')['RUNS'].transform('first')
all_data_df['MAX_RUNS'] = all_data_df['RUNS_INNINGS'] + all_data_df['RUNS_START']
all_data_df['RUNS_ROI'] = all_data_df['MAX_RUNS'] - all_data_df['RUNS']

all_data_df['BASES'] = all_data_df['BASE1_RUN_ID'].apply(str_to_value).astype(str) + \
                       all_data_df['BASE2_RUN_ID'].apply(str_to_value).astype(str) + \
                       all_data_df['BASE3_RUN_ID'].apply(str_to_value).astype(str)
all_data_df['STATE'] = all_data_df['BASES'] + all_data_df['OUTS_CT'].astype(str)

all_data_df['NRUNNER1'] = all_data_df.apply(first_occupied_after_play, axis=1)
all_data_df['NRUNNER2'] = all_data_df.apply(second_occupied_after_play, axis=1)
all_data_df['NRUNNER3'] = all_data_df.apply(third_occupied_after_play, axis=1)
all_data_df['NOUTS'] = all_data_df['OUTS_CT'] + all_data_df['EVENT_OUTS_CT']
all_data_df['NEW_BASES'] = all_data_df['NRUNNER1'].astype(str) + \
                           all_data_df['NRUNNER2'].astype(str) + \
                           all_data_df['NRUNNER3'].astype(str)
all_data_df['NEW_STATE'] = all_data_df['NEW_BASES'] + all_data_df['NOUTS'].astype(str)

filtered_df = all_data_df[(all_data_df['STATE'] == all_data_df['NEW_STATE']) | (all_data_df['RUNS_SCORED'] > 0)]
filtered_df = filtered_df[filtered_df['OUTS_INNINGS'] == 3]
x = filtered_df.groupby('STATE')['RUNS_ROI'].mean()
x_df = x.to_frame()
x_df.reset_index(level=0)

import ipdb
ipdb.set_trace()