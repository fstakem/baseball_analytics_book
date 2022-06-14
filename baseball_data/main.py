from pathlib import Path
from shutil import rmtree
from datetime import datetime

from baseball_data.lahman_fetcher import LahmanFetcher
from baseball_data.retrosheet_fetcher import RetrosheetFetcher


def generate_path() -> Path:
    file_path = Path(__file__).parent.resolve()
    current_dt = datetime.now()
    dt_str = current_dt.strftime('%m_%d_%Y__%H_%M')

    return file_path.parent / 'data' / dt_str


def create_output_path() -> Path:
    new_path = generate_path()

    if new_path.exists():
        rmtree(new_path)

    new_path.mkdir()

    return new_path


output_path = create_output_path()

lahman_path = output_path / 'lahman'
lahman_path.mkdir()
lahman_fetcher = LahmanFetcher()
lahman_fetcher.fetch_data(lahman_path)

retrosheet_path = output_path / 'retrosheet'
retrosheet_path.mkdir()
retrosheet_fetcher = RetrosheetFetcher()
retrosheet_fetcher.fetch_data(retrosheet_path)
