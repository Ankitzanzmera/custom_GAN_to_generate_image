from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir : Path
    source: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    preprocessed_dir: Path
