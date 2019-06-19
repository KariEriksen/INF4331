#!/usr/bin/python

"""
This program takes an argument, a string, searches through a given directory 
for files containing the string name.
Input in terminal: python find.py .filename $directory
"""
import sys
import os

search_word = str(sys.argv[1])
directory = str(sys.argv[2])

for root, dirs, files in os.walk(directory):
    for name in files:
	if search_word in name:
		print(os.path.join(root, name))


