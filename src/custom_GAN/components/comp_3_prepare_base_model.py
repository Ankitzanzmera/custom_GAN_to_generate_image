import sys,os
import numpy as np
from custom_GAN.utils.common import create_directories
from custom_GAN.utils.exception import CustomException
from custom_GAN.utils.logger import logger
from custom_GAN.entity.config_entity import PrepareBaseModelConfig
import keras
from keras.layers import Conv2D,LeakyReLU,Dropout,Flatten,Dense,Reshape,UpSampling2D
import matplotlib.pyplot as plt

class PrepareBaseModel:
    def __init__(self,config:PrepareBaseModelConfig):
        self.config = config
        create_directories([self.config.root_dir])

    @property
    def __build_discriminator_model__(self):
        model = keras.models.Sequential()

        model.add(Conv2D(32,5,input_shape = (28,28,1)))
        model.add(LeakyReLU(0.2))
        model.add(Dropout(0.4))

        model.add(Conv2D(64,5))
        model.add(LeakyReLU(0.2))
        model.add(Dropout(0.4))

        model.add(Conv2D(128,5))
        model.add(LeakyReLU(0.2))
        model.add(Dropout(0.4))

        model.add(Flatten())
        model.add(Dropout(0.2))
        model.add(Dense(1,activation="sigmoid"))

        return model
    
    @property
    def __build_generator_model__(self):
        model = keras.models.Sequential()

        model.add(Dense(7*7*128,input_dim = 128))
        model.add(LeakyReLU(0.2))
        model.add(Reshape((7,7,128)))  ## Takes in 2D

        model.add(UpSampling2D())
        model.add(Conv2D(128,5,padding = "same"))
        model.add(LeakyReLU(0.2))

        model.add(UpSampling2D())
        model.add(Conv2D(128,5,padding = "same"))
        model.add(LeakyReLU(0.2))

        model.add(Conv2D(128,5,padding = "same"))
        model.add(LeakyReLU(0.2))

        model.add(Conv2D(128,5,padding="same"))
        model.add(LeakyReLU(0.2))

        model.add(Conv2D(1,4,padding="same",activation="sigmoid"))

        return model

    def initiate_base_model_preparation(self):
        self.discriminator = self.__build_discriminator_model__
        self.generator = self.__build_generator_model__

        print(self.discriminator.summary())
        print(self.generator.summary())

        # predict_img = self.generator.predict(np.random.randn(4,128,1))
        # for idx,img in enumerate(predict_img):
        #     plt.imshow(np.squeeze(img))
        #     plt.savefig(f"subplot_{idx}.png")
        #     plt.close()
        

        keras.models.save_model(self.discriminator,self.config.discriminator_path)
        keras.models.save_model(self.generator,self.config.generator_path)

