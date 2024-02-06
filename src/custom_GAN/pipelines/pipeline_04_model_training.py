import sys
from custom_GAN.components.comp_04_model_training import ModelTraining
from custom_GAN.config.configuration import ConfigurationManager
from custom_GAN.utils.exception import CustomException
from custom_GAN.utils.logger import logger

class ModelTrainingPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            model_training_config = config.get_model_training_config()
            model_training = ModelTraining(config = model_training_config)
            model_training.initiate_GAN_training()
        except Exception as e:
            raise CustomException(e,sys)


STAGE_NAME = "Model Trainin"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*80)
    except Exception as e:
        raise CustomException(e,sys)