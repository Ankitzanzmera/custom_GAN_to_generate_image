import sys
from custom_GAN.utils.logger import logger
from custom_GAN.utils.common import CustomException
from custom_GAN.config.configuration import ConfigurationManager
from custom_GAN.components.comp_3_prepare_base_model import PrepareBaseModel

class PrepareBaseModelPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(prepare_base_model_config)
            prepare_base_model.initiate_base_model_preparation()
        except Exception as e:
            raise CustomException(e,sys)
        


STAGE_NAME = "Prepare Base Model"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*80)
    except Exception as e:
        raise CustomException(e,sys)