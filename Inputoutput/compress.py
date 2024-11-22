"""
Create a Python script that compresses all .txt files in a 
given directory using gzip compression. The compressed files should have 
the same name but with a .gz extension.
The script should also print out the compression ratio for each file.
"""
import json
import os
import shutil
import gzip
import base64
import re
import datetime

class TxtCompressor:
    def __init__(self, directory):
        self.directory = os.path.abspath(directory)
    
    def comp(self):
        #iterate all file one by one and create a .gzip file for every file.
        for filename in os.listdir(self.directory):
            if filename.endswith('.txt'):
                self.compress_file(filename)

    def compress_file(self, filename):
            input_file = os.path.join(self.directory, filename)
            output_file = input_file + '.gz'
        #copy file into gzip and compress it in the process
            with open(input_file, 'rb') as f_in:
                with gzip.open(output_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

    #find the compressed ratio
                # original_size = os.path.getsize(input_file)
                # compressed_file = os.path.getsize(output_file)
                # compression_ratio = (1 - compressed_file/original_size)*100
                # print (f"compression_ratio: {compression_ratio:.2f}%")
if __name__ == "__main__":
    directory_path = "/Users/vector8188/Desktop/Github_saumya043/python_code/Inputoutput"
    compressor = TxtCompressor(directory_path)
    compressor.comp()