#!/usr/bin/env python3
# Example to use mmap with concurrency
import concurrent.futures
import mmap
import pathlib
import pdb


MAX_THREAD_POOL_WORKERS = 10
RELEVANT_FILE_PATTERN = "*.txt"


def read_my_file(filepath):
    ip_address = None
    with open(filepath, "r") as file:
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
            try:
                ip_location_offset = mm.find(b"IP:")
                mm.seek(ip_location_offset)
                ip_string = mm.readline()
                ip_string = ip_string.decode("utf-8").strip()
                ip_address = ip_string.split("IP:")[1].strip()
            except (IndexError, ValueError):
                pass
    return ip_address


def read_all_files():
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREAD_POOL_WORKERS) as executor:
        p = pathlib.Path(".")
        # for relevant_file in p.glob(RELEVANT_FILE_PATTERN):
        #     executor.submit(lambda: read_my_file(relevant_file))
        results = executor.map(read_my_file, p.glob(RELEVANT_FILE_PATTERN))
        for result in filter(None, results):
            print(result)


if __name__ == "__main__":
    read_all_files()