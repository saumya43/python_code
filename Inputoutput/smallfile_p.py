"""
You have a directory containing 10,000 small text files. Each file is named like customer_1.txt, customer_2.txt, etc., and contains a single line with this format:

name,age,balance
John Doe,30,1000.50

Write a program that:
Reads all files
Finds customers with a balance greater than $500
Returns their names sorted by age
Handles any potential errors

"""
import os
from pathlib import Path
import logging
import shutil
import subprocess
import datetime
import subprocess
import concurrent.futures
import collections

RELEVANT_NAME = '*.txt'
MAX_WORKER = 10
logging.basicConfig(filename='smallfile.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')
logger = logging.getLogger(__name__)
HIGH_SPEND_CUSTOMERS = collections.deque()


def process_file(file):
    customers_list = []

    with open(file, 'r') as file_read:
        try:
            next(file_read)
            line = file_read.readline().strip()
            if line:
                name , age, salary = line.split(',')
                age = int(age)
                salary = float(salary)
                if salary > 500:
                    customers_list.append((name, age))
                    HIGH_SPEND_CUSTOMERS.append((name,age))
                    
        except(ValueError, AttributeError) as e:
            logging.error(f'{line} is not according to give standard or does not conatin values')
    # return customers_list
    return HIGH_SPEND_CUSTOMERS
    
#queue is thread safe
#micro optimisation and pre optimisiation is bad developer practise(YAGNI)
#file modes and when to use what

def read_all_files(directory):
    p = Path(directory)
    return p.glob(f'**/{RELEVANT_NAME}')

def process_all_files(directory):
    files_list = read_all_files(directory)
    # high_spend_customer =[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKER) as executor:
       HIGH_SPEND_COUSTOMERS = executor.map(process_file, files_list)

    #     high_spend_customers = [c for c_list in results for c in c_list]
    # return high_spend_customers



if __name__ == "__main__":
    path = "/Users/vector8188/Desktop/Github_saumya043/python_code/Inputoutput"
    # file_list = list(read_all_files(path))
    # customers_list = process_file(file_list)
    high_spend_customers =  process_all_files(path)
    # print(high_spend_customers)
    print(HIGH_SPEND_CUSTOMERS)
    
