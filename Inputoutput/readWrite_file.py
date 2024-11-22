"""
Write a python fuction that reads a text file , counts the occurrences of
each word(case-insensitive) and writes the result to new file named "word-count.txt" in the format
"word:count", sorted by count in descending order.
"""

import os
import datetime
import gzip
import shutil
import json
import re


wordDict = {}
with open('repeated.txt', 'r') as file:
    #convert text in lowercase letter
    text = file.read().lower()
    #remove all special character
    words = re.findall(r'\b\w+\b', text)
    for w in words:
        wordDict[w] = 1 + wordDict.get(w, 0)
    sortedFile = {k:v for k, v in sorted(wordDict.items(), key = lambda item:(item[1], item[0]))}
    with open('word-count.txt', 'w') as file:
        for key, value in sortedFile.items():
            file.write(f"{key}: {value}\n")
           
        

