import os,sys
from custom_GAN.utils.common import create_directories
from custom_GAN.utils.logger import logger
from custom_GAN.utils.exception import CustomException 
from custom_GAN.entity.config_entity import DataIngestionConfig
import gdown
from zipfile import ZipFile

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        create_directories([self.config.root_dir])

    @property
    def __download_file__(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                gdown.download(self.config.source,self.config.local_data_file)
                logger.info("Zip File Downloaded")
            else:
                logger.info("Zip file is Already Exists")
        except Exception as e:
            raise CustomException(e,sys)
    
    @property
    def __unzip_file__(self):
        try:
            if not os.path.exists(self.config.unzip_dir):
                with ZipFile(self.config.local_data_file,"r") as zip_ref:
                    zip_ref.extractall(self.config.unzip_dir)
                    logger.info("Zip file is extracted")
            else:
                    logger.info("Zip file is already extracted")
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_ingestion(self):
        self.__download_file__
        self.__unzip_file__