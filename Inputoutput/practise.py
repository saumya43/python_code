"""
Set up the basic structure of the LogAnalyzer class.
Implemented the find_log_files method to recursively search for log files in the given directory.
Added logging to track the progress and any potential issues.
Searches for log files in a specified directory and its subdirectories
The top 5 IP addresses with the most requests.
"""
import re
import os
import logging
from collections import Counter, defaultdict, deque
from pathlib import Path
import concurrent.futures

# Global variable
RELEVANT_FILE = "*.log"
MAX_WORKER = 4

def process_log_file(filename):
    ip = {}
    try:
        with open(filename, 'r') as file_read:
            for line in file_read:
                line = re.findall("\[(.*?)\]", line)
                if line:
                    ip[str(line[1])] = 1 + ip.get(line[1], 0)
        #         if line:
        #             ip_add[f'{line[1]}'] += 1
    except Exception as e:
        print(e)
    return ip

def find_all_file(directory):
    p = Path(directory)
    return list(p.glob(f'**/{RELEVANT_FILE}'))

def process_log_all_file(directory):
    ip_add = defaultdict(int)
    log_file = find_all_file(directory)
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKER) as executor:
            results = executor.map(process_log_file, log_file)
            # for ip_counts in results:
            #     for ip, count in ip_counts.items():
            #         ip_add[ip] += count

            # ip_add = [ip_counts.update(results) for ip_counts in results ]
    except(ValueError) as e:
        print(e)
    return most_called_ip(results)

def most_called_ip(results):
    most_visited_ip = []
    ip_add = defaultdict(int)
    for ip_counts in results:
                for ip, count in ip_counts.items():
                    ip_add[ip] += count
    ip_add = sorted(ip_add.items(), key = lambda item : item[1], reverse=True)  
    for i in ip_add:
        if len(most_visited_ip) < 5:
            most_visited_ip.append(i)

    return most_visited_ip


if __name__ == "__main__":
    path = '/Users/vector8188/Desktop/Github_saumya043/python_code/Inputoutput'
    # print(process_log_file('load_balancer_log.log'))
    print(process_log_all_file(path))
    # ip_address_dict = sorted(ip_address_dict.items(), key = lambda item : item[1], reverse=True)
    # for i in 

    # print(list(ip_add))
    # print(most_called_ip(ip_add))