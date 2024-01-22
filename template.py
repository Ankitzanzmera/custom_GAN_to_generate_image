from pathlib import Path
import os

project_name = "custom_GAN"

list_of_file = [
    ".github/workflows/.gitkeep",

    "config/config.yaml",

    f"src/{project_name}/components/__init__.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/pipelines/__init__.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/logger.py",
    f"src/{project_name}/utils/exception.py",

    f"src/{project_name}/constants/__init__.py",

    f"notebooks/trials.ipynb",

    "app.py",
    "main.py",
    "setup.py",

]

for filepath in list_of_file:
    filepath = Path(filepath)
    dirname,filename = os.path.split(filepath)

    if dirname != "":
        os.makedirs(dirname,exist_ok= True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as file:
            pass