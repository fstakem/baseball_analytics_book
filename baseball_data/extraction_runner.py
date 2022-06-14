from pathlib import Path

from baseball_data.extractor import Extractor

file_path = Path(__file__).parent.resolve()
data_path = file_path.parent / 'data' / 'test_1'
extractor = Extractor()
extractor.extract_all(data_path)