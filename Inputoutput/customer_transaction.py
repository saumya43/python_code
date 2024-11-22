"""
Log Analysis Task

Given a log file with the following format:
2024-10-24 09:15:30 | INFO | message="User login successful" user_id="ABC123" ip_address="192.168.1.100" session_id="sess_45678"
2024-10-24 09:15:35 | ERROR | message="Payment failed" transaction_id="TX789" amount="500.00" error_code="ERR_001" user_id="ABC123"

Requirements:

1. Parse and Extract:
   - Extract timestamp, log level, and key-value pairs from each log entry
   - Create a structured format (e.g., dictionary) for each log entry

2. Analysis Requirements:
   - Count occurrences of each log level (INFO, ERROR, WARNING)
   - Find all errors for a specific user_id
   - Calculate the time duration between first and last log
   - Find all failed payments (with amounts)
   - Track user session
"""
import os
import re
from collections import defaultdict


def customer_information(filename):
    level_count = defaultdict(int)
    
    user = []

    with open(filename, "r") as file_read:
        for line in file_read:
            message_list ={}
            if line:
                time, level, messages = line.strip().split(' | ')
                # message, user_id,  = re.compile[r'\"(.+?)\"']
                # message_list
                for item in messages.split('" '):
                        if '=' in item:
                            key, value = item.split('=')
                            value = value.strip('"')
                            message_list[key] = value
            user.append(message_list)
        return user
                
                
    return level_count
           
           


if __name__ == "__main__":
    filename = "customer_transaction.log"
    print(customer_information(filename))
    # data = [
    #     [2024-10-24 09:15:30 | INFO | message="User login successful" user_id="ABC123" ip_address="192.168.1.100" session_id="sess_45678" ],
    #     [2024-10-24 09:15:35 | ERROR | message="Payment failed" transaction_id="TX789" amount="500.00" error_code="ERR_001" user_id="ABC123"],
    #     [2024-10-24 09:16:10 | INFO | message="Order placed" order_id="ORD456" user_id="ABC123" total_amount="1200.00" items_count="3"]
    #     ]