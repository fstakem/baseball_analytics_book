from pathlib import Path

import wget


class LahmanFetcher(object):
    base_url: str = 'https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags'
    zip_files: list[str] = ['v2016.1.zip', 'v2017.2.zip', 'v2018.1.zip', 'v2019.2.zip', 'v2020.1.zip', 'v2021.2.zip',
                            'v2022.2.zip']

    def __init__(self) -> None:
        pass

    def fetch_data(self, output_path: Path, fetch_all: bool = True) -> None:
        urls = self._get_urls()
        self._download_files(output_path, urls)

    def _get_urls(self) -> list[str]:
        return [f'{self.base_url}/{z}' for z in self.zip_files]

    def _download_files(self, output_path: Path, urls: list[str]) -> None:
        for url in urls:
            print(f'Downloading {url}...')
            filename = wget.download(url, out=str(output_path))  # noqa: F841
