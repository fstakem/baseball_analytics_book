from pathlib import Path
from typing import Optional
from shutil import move

from zipfile import ZipFile


class Extractor(object):

    def extract_all(self, root_path: Path) -> None:
        root_path = root_path
        archive_path = self._get_archive_path(root_path)

        if not archive_path:
            print('Archive path is not empty')

            return

        lahman_path = root_path / 'lahman'
        self.extract_lahman(lahman_path, archive_path)

        retrosheet_path = root_path / 'retrosheet'
        self.extract_retrosheet(retrosheet_path, archive_path)

    def extract_lahman(self, data_path: Path, archive_path: Path) -> None:
        archive_path = archive_path / 'lahman'

        archive_path.mkdir()

        for p in data_path.iterdir():
            self._extract_and_move_file(p, archive_path)

    def extract_retrosheet(self, data_path: Path, archive_path: Path) -> None:
        sub_dir = ['box_score', 'gamelog', 'play_by_play']
        archive_path = archive_path / 'retrosheet'

        archive_path.mkdir()

        for s in sub_dir:
            path = data_path / s

            for p in path.iterdir():
                self._extract_and_move_file(p, archive_path)

    def _get_archive_path(self, root_path: Path) -> Optional[Path]:
        archive_path = root_path / 'archive'

        if archive_path.exists():
            return None

        archive_path.mkdir()

        return archive_path

    def _extract_and_move_file(self, file_path: Path, archive_path: Path) -> None:
        print(file_path)

        with ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(file_path.parent)

        dst_path = archive_path / file_path.name
        print(f'Moving file\n\tfrom: {file_path}\n\tto: {dst_path}')
        move(str(file_path), str(dst_path))
