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


@dataclass(frozen = True)
class PrepareBaseModelConfig:
    root_dir: Path
    generator_path: Path
    discriminator_path: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    preprocessed_dir: Path
    generator_path: Path
    discriminator_path: Path
    trained_generator_path: Path
    trained_discriminator_path: Path
