"""
Step 1: Define the problem
We need to create a Python script that can:

Recursively search through a directory structure
Identify and read all YAML files
Locate a particular key (e.g., 'database_version')
Update its value to a new specified version (e.g., '2.1')
Save the changes back to the files
"""
import os
import shutil
from datetime import datetime
import re
import yaml
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(level)s-%(message)s')


def update_yaml_files(root_dir, key_to_update, new_value):
    updated_files = 0
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        #convert yaml file into standar pyton dict
                        data = yaml.safe_load(f)
                        if isinstance(data, dict) and key_to_update in data:
                            data[key_to_update] = new_value
                            with open(file_path, 'w') as f:
                                yaml.dump(data, f, default_flow_style=False)
                            updated_file += 1
                            
                        else:
                            logging.info(f"key not found {key_to_update}")
                except Exception as e:
                       logging.error(f"Error processing {file_path}: {str(e)}")
    return updated_files

if __name__ == '__main__':
    root_directory = "/Users/vector8188/Desktop/Github_saumya043/python_code/Inputoutput"
    new_value = "2.9"
    key_to_update = "database_version"
    total_updated = update_yaml_files(root_directory, key_to_update, new_value)
    print(total_updated)

