"""
Set up the basic structure of the LogAnalyzer class.
Implemented the find_log_files method to recursively search for log files in the given directory.
Added logging to track the progress and any potential issues.
Set up the command-line argument parsing
Searches for log files in a specified directory and its subdirectories.
Analyzes the logs from the past 24 hours.

Calculates and reports the following metrics:
a. The top 3 services with the highest average response times.
b. The percentage of 4xx and 5xx status codes for each service.
c. The top 5 IP addresses with the most requests.
d. The busiest hour of the day (most requests).
Identifies any services that have had more than 5 consecutive 500 status codes.
Generates a summary report and saves it as a Markdown file.

Additional requirements:

The script should be efficient and able to handle large log files (up to 1GB).
It should use multiprocessing to parallelize the log analysis for better performance.
Implement proper error handling and logging within your script.
The script should accept command-line arguments for the log directory and output file path.

To make your solution even more impressive, consider adding these optional features:

Use a generator to read log files line by line, reducing memory usage for large files.
Implement a simple caching mechanism to store partially processed results, allowing the script to resume analysis if interrupted.
Add unit tests for your key functions to ensure reliability.
"""
from asyncio import constants
from ipaddress import ip_address
import os
import json
import shutil
from datetime import datetime, timedelta
import argparse
import multiprocessing
from collections import defaultdict, Counter
import heapq
import logging
import re

class LogAnalyzer:
    def __init__(self, log_dir, output_file):
        # [2024-10-19 14:23:45] [192.168.1.100] [auth-service] [235ms] [200] [/api/login]
        self.expression = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\] \[([\w-]+)\] \[(\d+)ms\] \[(\d+)\] \[(.+)\]')
        output_file = self.output_file
        #calculate time slack for 24 hours
        self.time_cutoff = datetime.now() - datetime.timedelta(hours=24)
        #define logger
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getlogger(__name__)

    #find load balancer log file in a directory
    def find_log_files(self):
        self.logger.info(f"Searching for log files in a directory {self.log_dir}")
        logfiles = []
        for root, _ , files in os.walk(self.log_dir):
             for file in files:
                 if file.endswith(".log"):
                     logfiles.append(os.path.join(root, file))
        self.logger.info(f"found {len(logfiles)} log files")
        return logfiles
    
    #process each log file to create metrics according to the log analyze.
    def process_log_file(self, logfile):
        metric = {
            'service_response_time' : defaultdict(list),
            'status_codes' : defaultdict(Counter),
            'ip_requests': Counter(),
            'hourly_request': Counter(),
            'consecutive_500s':  defaultdict(int)
        }
        
        with open(logfile, 'r') as file:
            for line_number, line in enumerate(file, 1):
                match = self.expression.match(line)
                if match:
                    try:
                        timestamp, ip, service, responseTime, status, path = match.groups()
                        timestamp = datetime.striptime(timestamp, '%Y-%m-%d %H:%M:%S')
                        if timestamp < self.time_cutoff:
                            continue
                        responseTime = int(status[:-2])
                        status = int(status)
                        metric['service_response_time'][service].append(responseTime)
                        metric['status_codes'][service][status] += 1
                        metric['ip_requests'][ip] += 1
                        metric['hourly_requests'][timestamp.hour] += 1

                        if status == 500:
                            metric['consecutive_500s'][service] += 1
                            if metric['consecutive_500s'][service] > 5:
                                self.logger.info(f"Service {service} has more than 5 consecutive 500 status code")
                        else:
                            metric['consecutive_500s'][service] = 0
            
                    except (ValueError, AttributeError) as e:
                        self.logger.warning(f"error in {line_number} in {line} of {logfile} : {e}")
                        self.logger.warning(f"problmatic_line:{line.strip()}")
                else:
                    self.logger.warning(f"there is no match in the {file} for {line.strio()}")
        return metric

    def analyze_logs(self):
        logfiles = self.find_log_files()
        with multiprocessing.Pool() as pool:
            results = pool.map(self.process_log_files, logfiles)
        aggregated_metrics = {
            'service_response_time' : defaultdict(list),
            'status_codes' : defaultdict(Counter),
            'ip_requests': Counter(),
            'hourly_request': Counter(),
            'consecutive_500s':  defaultdict(int)
        }
        
        for result in results:
            for service, times in result['service_response_times'].items():
                aggregated_metrics['service_response_times'][service].extend(times)
            for service, code in result['status_codes'].items():
                aggregated_metrics['status_code'][service].update(code)
            aggregated_metrics['ip_requests'].update(result['ip_requests'])
            aggregated_metrics['hourly_requests'].update(result['hourly_requests'])
            for service, count in 'consecutive_500s'.items():
                aggregated_metrics['consecutive_500s'][service] = max(aggregated_metrics['consecutive_500s'][service], count)
                        
        return aggregated_metrics
                        
def generate_report(self, aggregated_metrics):
        report = "Log Analysis Report\n=====================\n\n"

        # Top 3 services with highest average response times
        avg_response_times = {
            service: sum(times)/len(times) 
            for service, times in aggregated_metrics['service_response_times'].items()
        }
        top_3_response_times = sorted(avg_response_times.items(), key=lambda x: x[1], reverse=True)[:3]
        
        report += "Top 3 Services by Average Response Time:\n"
        for service, avg_time in top_3_response_times:
            report += f"  {service}: {avg_time:.2f}ms\n"

        # Error rates
        report += "\nError Rates by Service:\n"
        for service, codes in aggregated_metrics['status_codes'].items():
            total = sum(codes.values())
            error_rate = sum(codes[status] for status in codes if status >= 400) / total
            report += f"  {service}: {error_rate:.2%}\n"

        # Top 5 IP addresses
        top_5_ips = aggregated_metrics['ip_requests'].most_common(5)
        report += "\nTop 5 IP Addresses by Request Count:\n"
        for ip, count in top_5_ips:
            report += f"  {ip}: {count}\n"

        # Busiest hour
        busiest_hour = max(aggregated_metrics['hourly_requests'], key=aggregated_metrics['hourly_requests'].get)
        report += f"\nBusiest Hour: {busiest_hour:02d}:00 with {aggregated_metrics['hourly_requests'][busiest_hour]} requests\n"

        # Services with more than 5 consecutive 500 errors
        problem_services = [service for service, count in aggregated_metrics['consecutive_500s'].items() if count > 5]
        if problem_services:
            report += "\nServices with More Than 5 Consecutive 500 Errors:\n"
            for service in problem_services:
                report += f"  {service}\n"
        else:
            report += "\nNo services had more than 5 consecutive 500 errors.\n"

        return report

        def run_analysis(self):
            aggregated_metrics = self.analyze_logs()
            report = self.generate_report(aggregated_metrics)
            print(report)

# Usage example
if __name__ == "__main__":
    log_dir = "/Users/vector8188/Desktop/Github_saumya043/python_code/Inputoutput"  # Replace with your actual log directory
    analyzer = LogAnalyzer(log_dir)
    analyzer.run_analysis()


