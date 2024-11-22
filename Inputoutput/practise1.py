# The top 5 IP addresses with the most requests.
import re 
import os
import logging
from  pathlib  import Path
from collections import defaultdict
from concurrent import futures

RELEVANT_PATTERN = "*.log"
def read_all_file(path):
    p = Path(path)
    return p.glob(f'**/{RELEVANT_PATTERN}')
    
def process_File(file):
    ip_dict = defaultdict(int)
    try:
        with open(file, 'r') as read_file:
            for line in read_file:
                line = re.findall("\[(.*?)\]", line)
                if line:
                    ip = str(line[1])
                    ip_dict[str(line[1])] += 1
    except Exception as e:
        print(e)
    return ip_dict
            # if line:
            #     ip = line[1]
            #     print(ip)

def process_all_file(path):
    log_files = read_all_file(path)
    with futures.ThreadPoolExecutor(max_workers=2) as executor:
       result =  executor.map(process_File, log_files)
    return most_called_ip(result)

def most_called_ip(all_ip_count):
    most_ip_count = defaultdict(int)
    ip_add = []
    for IPcount in all_ip_count:
        for ip, count in IPcount.items():
            most_ip_count[ip] += count
    most_ip_count = sorted(most_ip_count.items(), key = lambda item : item[1], reverse= True)
    for k, v in most_ip_count:
        while len(ip_add) < 5:
            ip_add.append(k)
    return ip_add


    


if __name__ == "__main__":
    path = "/Users/vector8188/Desktop/Github_saumya043/python_code/Inputoutput"
    # file = "load_balancer.log"
    # print(process_File(file))
    print(process_all_file(path))


    # print(list(read_all_file(path)))