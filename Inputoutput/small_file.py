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
import logging
from pathlib import Path
import pdb
import concurrent.futures
import itertools

RELEVANT_FILE = "*.txt"
MAX_WORKER=10
# FileName = "age.txt"
logging.basicConfig(filename='smallfile.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')
logger = logging.getLogger(__name__)


# find all files in a directory
def read_all_file(directory): 
    # customers_file = [] 
    p = Path(directory) 
    return p.glob(f'**/{RELEVANT_FILE}')
    # for root, _, files in os.walk(directory):
    #     try:
    #         for file in files:

    #             if file.endswith(RELEVANT_FILE):
    #                 yield file
    #                 customers_file.append(os.path.join(root, file)) #no need if using yield

    #     except(ValueError) as e:
    #         print (f"no file exist")
    # return customers_file
   
#find all customers from the file
def find_all_customers(directory):
    customer_list = read_all_file(directory)
    # for  c in customer_list:
    #     yield from process_file(c)
    # for file in customer_list:
    #     
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKER) as executor:
        results = executor.map(process_file, customer_list)
        high_customers = [ c for c_list in results for c in c_list ]
    
        
    return high_customers   

# process each file in the directory
def process_file(Filename):
    customer = []
    with open(Filename, "r") as file_read:
        try:
            next(file_read)
            line = file_read.readline().strip()
            if line:
                name, age, balance = line.split(',')
                age = int(age)
                balance = float(balance)
                if balance > 500:
                    # yield (name, age)
                    customer.append((name, age))
        except(ValueError, AttributeError) as e:
            logging.error(f" does not contain the below pattern:{e}") 
    return customer





if __name__ == "__main__":
    path = "/Users/vector8188/Desktop/Github_saumya043/python_code/Inputoutput/"
    # print(read_all_file(path))
    results = find_all_customers(path)
    # print(results)
    print(sorted(results, key= lambda x: x[1]))

            