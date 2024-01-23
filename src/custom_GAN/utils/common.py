import os,sys
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from typing import Any
from custom_GAN.utils.exception import CustomException
from pathlib import Path

@ensure_annotations
def read_yaml(path:Path) -> ConfigBox:
    try:
        with open(path,"r") as yaml_file:
            content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml is Empty")
    except Exception as e:
        raise CustomException(e,sys)
    

@ensure_annotations
def create_directories(dir_list: list):
    for path in dir_list:
        os.makedirs(path,exist_ok= True)