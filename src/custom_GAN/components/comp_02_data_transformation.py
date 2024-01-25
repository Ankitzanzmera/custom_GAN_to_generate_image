import os,sys
from pathlib import Path
from custom_GAN.utils.logger import logger
from custom_GAN.utils.common import create_directories
from custom_GAN.utils.exception import CustomException
from custom_GAN.entity.config_entity import DataTransformationConfig
from keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf
from tqdm import tqdm
import pickle

class DataTransformation:
    def __init__(self,config : DataTransformationConfig):
        self.config = config
        create_directories([self.config.root_dir])

    def __load_img__(self,image_path):
        image = tf.io.read_file(image_path)
        image = tf.image.decode_image(image,channels = 1)
        return image

    def _bytes_feature(self,value):
        return tf.train.Feature(bytes_list=tf.train.BytesList(value=[tf.io.encode_jpeg(value).numpy()]))

    def initiate_data_transformation(self):
        try:
            image_path_list = [str(os.path.join(self.config.data_dir,filepath)) for filepath in os.listdir(self.config.data_dir)]

            dataset = tf.data.Dataset.from_tensor_slices(image_path_list)
            dataset = dataset.map(self.__load_img__)
            dataset = dataset.cache()
            dataset = dataset.shuffle(buffer_size = len(image_path_list))
            dataset = dataset.batch(128)
            dataset = dataset.prefetch(buffer_size = 128)

            tf.data.Dataset.save(dataset,self.config.preprocessed_dir)

 



        except Exception as e:
            raise CustomException(e,sys)


