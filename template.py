import os
from pathlib import Path

import logging
level_name = logging.INFO
logging.basicConfig(level= level_name,format="[%(asctime)s]:  %(message)s:")


#Creating the folders and files for implementation
Project_name = "Fraud_transaction_detection"

list_of_files = [
    f'src/{Project_name}/__init__.py',
    f'src/{Project_name}/components/__init__.py',
    f'src/{Project_name}/utils/__init__.py',
    f'src/{Project_name}/utils/common.py',
    f'src/{Project_name}/config/__init__.py',
    f'src/{Project_name}/config/configaration.py',
    f'src/{Project_name}/pipeline/__init__.py',
    f'src/{Project_name}/entity/__init__.py',
    f'src/{Project_name}/entity/config_entity.py',
    f'src/{Project_name}/constants/__init__.py',
    "config/config.yaml",
    "param.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirement.txt",
    "setup.py",
    "research/trials.ipnb",
    "templates/index.html"
]

for filepath in list_of_files:
    #converting the strpath to Path according to your os
    file_path = Path(filepath) 
    file_dir, filename = os.path.split(file_path)
    #create the directory
    if file_dir != "":
        os.makedirs(file_dir,exist_ok= True)
        logging.info(f"creating directory: {file_dir} for the file{filename}")
    #create the files if the file is not exist and
        #  if exist then check that the file is not containing any code.
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} is already exists")


