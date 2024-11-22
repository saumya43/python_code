import json
import re
import datetime
import shutil
import os

with open('logfile.txt', "r") as file:
    content = file.read()
print(content)

# check file whether it exists before opening it in python
if os.path.exists('example.txt'):
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
else:
    print(" file does not exit ")

