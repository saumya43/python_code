"""
Step 1: Define the problem
We need to create a Python script that can:

Recursively search through a directory structure
Identify and read all YAML files
Locate a particular key (e.g., 'database_version')
Update its value to a new specified version (e.g., '2.1')
Save the changes back to the files
#approach
"""
#import important packages
import os
import re
import yaml
from datetime import timedelta
from collections import defaultdict, Counter

# find all yaml files
# def find_yaml_file():
update_file = 0
def update_yaml_content(data, key_to_update, new_value):
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key_to_update:
                data[k] = new_value
            elif isinstance(v, (dict,list)):
               update_yaml_content(v, key_to_update, new_value)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
               update_yaml_content(item, key_to_update, new_value)
    return data
        


def process_yaml_file(file, key_to_update, new_value):
    with open (file, "r") as file_read:
        data = yaml.safe_load(file_read)
        update_data = update_yaml_content(data, key_to_update, new_value)
    with open(file, 'w') as file_write:
        yaml.dump(update_data , file_write, default_flow_style=False)

def find_yaml_file(path, key_to_update, new_value):
    
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".yml") or file.endswith(".yaml"):
                file_path = os.path.join(root, file)
                try:
                    
                        if process_yaml_file(file_path, key_to_update, new_value):
                            update_file += 1
                except(ValueError, AttributeError) as e:
                    print(f"{str(e)}")
    return update_file
        

    

# def nested_dict()
# def update_file()
if __name__ == "__main__":
    path = "/Users/vector8188/Desktop/Github_saumya043/python_code/Inputoutput/"
    key_to_update = "database_version"
    new_value = "2.9"
    find_yaml_file(path,key_to_update, new_value)