import sys
import logging
import os
from datetime import datetime

dir_name = f"{datetime.now().strftime('%d_%m_%y')}"
dir_path  = os.path.join(os.getcwd(),"logs",dir_name)
os.makedirs(dir_path,exist_ok=True)

file_name = f"{datetime.now().strftime('%H_%M_%S')}.log"
file_path = os.path.join(dir_path,file_name)

logging.basicConfig(
    level= logging.INFO,
    format = "[ %(asctime)s - %(module)s - %(lineno)d - %(message)s ]",
    handlers = [
        logging.FileHandler(file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("custom_gan_logger")
