from sys import argv

script, directory_name = argv

import os

file_list = os.listdir(directory_name)

file_info = []
file_ext = []

for w in file_list:
	
	file_info = w.split('.')
	file_ext.append(file_info[1])

def word_frequency(fileext):
	frequency = {}

	for w in fileext:
		frequency[w] = frequency.get(w, 0) + 1
	return frequency

print word_frequency(file_ext)


# Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.
