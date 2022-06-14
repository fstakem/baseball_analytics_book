from pathlib import Path

import wget


class RetrosheetFetcher(object):
    base_url: str = 'https://www.retrosheet.org'
    pbp_event_files: list[str] = ['1910seve.zip', '1920seve.zip', '1930seve.zip', '1940seve.zip', '1950seve.zip',
                                  '1960seve.zip', '1970seve.zip', '1980seve.zip', '1990seve.zip', '2000seve.zip',
                                  '2010seve.zip', '2020seve.zip', 'allpost.zip']
    box_score_event_files: list[str] = ['1900sbox.zip', '1910sbox.zip', '1920sbox.zip', '1930sbox.zip',
                                        '1940sbox.zip', '1950sbox.zip']
    game_log_files: list[str] = ['gl1871_2021.zip', 'glws.zip', 'glwc.zip', 'gldv.zip', 'gllc.zip']

    def __init__(self) -> None:
        pass

    def fetch_data(self, output_path: Path, fetch_all: bool = False) -> None:
        pbp_urls = self._get_pbp_urls()
        pbp_path = output_path / 'play_by_play'
        pbp_path.mkdir()
        self._download_files(pbp_path, pbp_urls)

        box_score_urls = self._get_box_score_urls()
        box_score_path = output_path / 'box_score'
        box_score_path.mkdir()
        self._download_files(box_score_path, box_score_urls)

        gamelog_urls = self._get_gamelog_urls()
        gamelog_path = output_path / 'gamelog'
        gamelog_path.mkdir()
        self._download_files(gamelog_path, gamelog_urls)

    def _get_pbp_urls(self) -> list[str]:
        return [f'{self.base_url}/events/{p}' for p in self.pbp_event_files]

    def _get_box_score_urls(self) -> list[str]:
        return [f'{self.base_url}/events/{b}' for b in self.box_score_event_files]

    def _get_gamelog_urls(self) -> list[str]:
        return [f'{self.base_url}/gamelogs/{g}' for g in self.game_log_files]

    def _download_files(self, output_path: Path, urls: list[str]) -> None:
        for url in urls:
            print(f'Downloading {url}...')
            filename = wget.download(url, out=str(output_path))  # noqa: F841
