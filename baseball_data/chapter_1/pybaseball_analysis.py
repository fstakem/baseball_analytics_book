from pathlib import Path

import pandas as pd
from pybaseball import statcast, playerid_lookup, statcast_pitcher, statcast_batter, pitching_stats, batting_stats, standings

# Original data
# df = statcast(start_dt='2021-04-01', end_dt='2021-11-01')
acuna_player_df = playerid_lookup('acuna')
olson_player_df = playerid_lookup('olson', 'matt')
olson_id = olson_player_df['key_mlbam'][0]
olson_df = statcast_batter('2021-04-01', '2021-11-01', olson_id)
pitching_df = pitching_stats(2021, 2021)
batting_df = batting_stats(2021, 2021)
standings_list = standings(2022)

sc_path = Path('/home/fstakem/projects/baseball_data/data/05_04_2022__21_17/statcast/2021_full_season.csv')
sc_df = pd.read_csv(sc_path, index_col=0)
import ipdb
ipdb.set_trace()