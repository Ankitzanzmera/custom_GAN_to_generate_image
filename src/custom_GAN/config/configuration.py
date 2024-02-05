from pathlib import Path
from custom_GAN.constants import *
from custom_GAN.utils.common import read_yaml,create_directories
from custom_GAN.entity.config_entity import (DataIngestionConfig,
                                            DataTransformationConfig,
                                            PrepareBaseModelConfig)


class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILEPATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config.root_artifacts])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        temp_config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir = temp_config.root_dir,
            source = temp_config.source,
            local_data_file = temp_config.local_data_file,
            unzip_dir = temp_config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        temp_config = self.config.data_transformation

        data_transformation_config = DataTransformationConfig(
            root_dir = temp_config.root_dir,
            data_dir=temp_config.data_dir   ,
            preprocessed_dir = temp_config.preprocessed_data_file
        )
    
        return data_transformation_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        temp_config = self.config.prepare_base_model

        base_model_config = PrepareBaseModelConfig(
            root_dir = temp_config.root_dir,
            generator_path = temp_config.generator_path,
            discriminator_path = temp_config.discriminator_path
        )
        
        return base_model_config