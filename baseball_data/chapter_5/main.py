from pathlib import Path

import pandas as pd

file_path = Path(__file__).parent
project_path = Path(__file__).parent.parent.parent.resolve()
all_data_path = file_path / 'all2016.csv'
fields_path = file_path / 'fields.csv'


def str_to_value(row: str) -> str:
    if len(row) > 0:
        return '1'

    return '0'


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
                       all_data_df['BASE3_RUN_ID'].apply(str_to_value).astype(str) + \
                       ' ' + \
                       all_data_df['OUTS_CT'].astype(str)

# all_data_df['BASES'] = (all_data_df['BASE1_RUN_ID'])
# np.where(all_data_df['BASE1_RUN_ID'].str.len() > 0, 1, 0)


import ipdb
ipdb.set_trace()