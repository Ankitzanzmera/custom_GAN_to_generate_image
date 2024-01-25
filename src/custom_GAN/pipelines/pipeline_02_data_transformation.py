import sys
from custom_GAN.utils.exception import CustomException
from custom_GAN.utils.logger import logger
from custom_GAN.components.comp_02_data_transformation import DataTransformation
from custom_GAN.config.configuration import ConfigurationManager

class DataTransformationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformaton = DataTransformation(data_transformation_config)
            data_transformaton.initiate_data_transformation()
        except Exception as e:
            raise CustomException(e,sys)
        

STAGE_NAME = "Data Transformation"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*80)
    except Exception as e:
        raise CustomException(e,sys)