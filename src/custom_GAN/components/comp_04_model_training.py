from custom_GAN.utils.common import create_directories
from custom_GAN.utils.logger import logger
from custom_GAN.entity.config_entity import ModelTrainingConfig
import keras
from keras import Model
import tensorflow as tf

class CustomGAN(Model):
    def __init__(self,generator,discriminator,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.generator = generator
        self.discriminator = discriminator

    def compile(self,generator_optimizer,discriminator_optimizer,generator_loss,discriminator_loss,*args,**kwargs):
        super().compile(*args,**kwargs)

        self.generator_optimizer = generator_optimizer
        self.discriminator_optimizer = discriminator_optimizer
        self.generator_loss = generator_loss
        self.discriminator_loss = discriminator_loss

    def train_step(self,batch):
        real_images = batch
        fake_images = self.generator(tf.random.normal((128,128,1)),training = False)

        ## Train Discriminator
        with tf.GradientTape() as discriminator_tape:
            y_hat_real = self.discriminator(real_images,training = True)
            y_hat_fake = self.discriminator(fake_images,training = False)
            y_hat_real_fake = tf.concat([y_hat_real,y_hat_fake],axis = 0)

            ## Create label for real and fake images
            y_real_fake = tf.concat([tf.zeros_like(y_hat_real),tf.ones_like(y_hat_fake)],axis = 0)

            ## Adding some noise to actual o/t
            noise_real = 0.15 * tf.random.uniform(tf.shape(y_hat_real))
            noise_fake = -0.15 * tf.random.uniform(tf.shape(y_hat_fake))
            y_real_fake += tf.concat([noise_real,noise_fake],axis = 0)

            ## calculate loss
            total_discriminator_loss = self.discriminator_loss(y_real_fake,y_hat_real_fake)
        
        ## Apply Back propaga
        discriminator_gradient = discriminator_tape.gradient(total_discriminator_loss,self.discriminator.trainable_variables)
        self.discriminator_optimizer.apply_gradients(zip(discriminator_gradient,self.discriminator.trainable_variables))


        ## Train Generator
        with tf.GradientTape() as generator_tape:

            ## Generate Image
            generated_images = self.generator(tf.random.normal((128,128,1)),training = True)

            ## Create Predicted Images
            predicted_labels = self.discriminator(generated_images,training = False)
            
            ## Calc Loss
            total_generator_loss = self.generator_loss(tf.zeros_like(predicted_labels),predicted_labels)

        
        ## Apply Back Prop
        generator_gradient = generator_tape.gradient(total_generator_loss,self.generator.trainable_variables)
        self.generator_optimizer.apply_gradients(zip(generator_gradient,self.generator.trainable_variables))

        return {"Discriminator_loss":total_discriminator_loss,"Generator_loss":total_generator_loss}
    
    def save_trained_model(self,generator_path,discriminator_path):
        keras.models.save_model(self.generator,generator_path)
        keras.models.save_model(self.discriminator,discriminator_path)



class ModelTraining:
    def __init__(self,config: ModelTrainingConfig):
        self.config = config
        create_directories([self.config.root_dir])

    @property
    def __load_model__(self):
        generator = keras.models.load_model(self.config.generator_path)
        discriminator = keras.models.load_model(self.config.discriminator_path)
        return generator,discriminator

    @property
    def __load_dataset__(self):
        dataset = tf.data.Dataset.load(self.config.preprocessed_dir)
        return dataset

    @property
    def __optimizers__(self):
        generator_optimizer = keras.optimizers.legacy.Adam(learning_rate = 0.0001)
        discriminator_optimizer = keras.optimizers.legacy.Adam(learning_rate = 0.00001)
        return generator_optimizer,discriminator_optimizer

    @property
    def __losses__(self):
        generator_loss = keras.losses.BinaryCrossentropy()
        discriminator_loss = keras.losses.BinaryCrossentropy()
        return generator_loss,discriminator_loss
    
    def initiate_GAN_training(self):

        generator,discriminator = self.__load_model__
        dataset = self.__load_dataset__

        model = CustomGAN(generator,discriminator)

        generator_optimizer,discriminator_optimizer = self.__optimizers__
        generator_loss,discriminator_loss = self.__losses__

        model.compile(generator_optimizer,discriminator_optimizer,generator_loss,discriminator_loss)


        model.fit(dataset,epochs = 1)
        logger.info("Training has been Completed")

        model.save_trained_model(self.config.trained_generator_path,self.config.trained_discriminator_path)
        logger.info("Trained Model Saved")









