import sys
from custom_GAN.utils.logger import logger
from custom_GAN.utils.exception import CustomException
from custom_GAN.config.configuration import ConfigurationManager
from custom_GAN.components.comp_01_data_ingestion import DataIngestion

class DataIngestionPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e,sys)
        
STAGE_NAME = "Data Ingestion"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*80)
    except Exception as e:
        raise CustomException(e,sys)