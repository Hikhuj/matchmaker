#! /usr/bin/env python
# -*- coding: utf-8 -*-
# version: 1.0

'''

	@author-name: Roger Ulate Rivera
	@author-creation-date: 05/11/2018 (mm/dd/yyyy)
	@custom imported libraries: colorama ---> https://pypi.org/project/colorama/

Pending to check:

Script must check if file exists

'''

# Importe de modulos
import pdb
# pdb.set_trace()
import csv
import os
#import glob
#import sys
from colorama import *
init()


# Variable list
variable_list_messages = ['Please provide the file that works as base document...',
							'Please provide the file that will be compare...',
							'Copy and paste the file name to be used (use the format ==> fileName.extension): ']

# http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html

def message_id_matcher_welcome():
	print("")
	print(Fore.YELLOW + "* --------------------------------------------------- *")
	print(Fore.YELLOW + "|                                                     |")
	print(Fore.YELLOW + "|                 Welcome to Id Matcher               |")
	print(Fore.YELLOW + "|                                                     |")
	print(Fore.YELLOW + "* --------------------------------------------------- *")
	print("")
	print(Style.RESET_ALL)

def message_id_matcher_bye():
	print("")
	print(Fore.GREEN + "* --------------------------------------------------- *")
	print(Fore.GREEN + "|                                                     |")
	print(Fore.GREEN + "|      Done, please check clean.csv file. Bye!!!      |")
	print(Fore.GREEN + "|                                                     |")
	print(Fore.GREEN + "* --------------------------------------------------- *")
	print("")
	print(Style.RESET_ALL)

def verify_if_file_in_path_exists(file_path):
	# Function read where the file is on the root project only.
	result = os.path.isfile(file_path)
	return result

def request_file_name():
	result = get_relative_path()
	return result

# Request compression of relative paths
def get_relative_path():
	# Variables
	result = ""
	absFilePath = ""

	print("")

	# Request the name of the file to work
	file_name = input(variable_list_messages[2])
	is_a_csv = validator_check_file_extension(file_name)

	# Verification
	if is_a_csv == True:
		absFilePath = os.path.abspath(file_name)
		csv_exists = verify_if_file_in_path_exists(absFilePath)

		# If the file exist
		if csv_exists == True:
			result = absFilePath
		else:
			print(Fore.RED + "* --------------------------------------------------- *")
			print(Fore.RED + "|    The file you are trying to add is not a '.csv'   |")
			print(Fore.RED + "|           Please try adding a CSV file only         |")
			print(Fore.RED + "* --------------------------------------------------- *")
			print(Style.RESET_ALL)
			get_relative_path()
	
	# If the file is not a .csv extension
	else:
		print(Fore.RED + "* --------------------------------------------------- *")
		print(Fore.RED + "|    The file you are trying to add is not a '.csv'   |")
		print(Fore.RED + "|           Please try adding a CSV file only         |")
		print(Fore.RED + "* --------------------------------------------------- *")
		print(Style.RESET_ALL)
		get_relative_path()

	print("")

	return result

def validator_check_file_extension(csv_file_name):
	result = False

	if csv_file_name.lower().endswith('.csv'):
		result = True

	return result

def csv_file_reader(source_file_path, error_file_path):
	with open(source_file_path, 'r', encoding='utf-8') as csv_file:
		csv_reader = csv.reader(csv_file)

		position = 1

		for row in csv_reader:
			# Set default list will be attached to row null
			additional_info = []
			print("-------> Processing line: " + str(position))

			# Search for Id on errors.csv file or file of choice, if find something, will return list of content
			additional_info = search_id_in_file(row[0], error_file_path, position)
			
			# Add to each row any data that appears on previous result
			row.extend(additional_info)

			write_on_file(row)

			# Increase row position to read
			position += 1

def search_id_in_file(line_id, error_file_path, position):
	result = []

	# Read the CSV where the code will pull data if it match in file_B
	with open(error_file_path, 'r', encoding='utf-8') as file:
		file_B = csv.reader(file, delimiter=',')

		# Read each row of the CSV
		for row in file_B:
			if row[0] == line_id:
				result = row
				print(">>> Id found: " + str(position) + ", matching...")
				print(".")
				break

	return result

def write_on_file(row):
	with open ("clean.csv", 'a', encoding='utf-8') as file:
		file = csv.writer(file, delimiter=',')
		file.writerow(row)

def interactive_menu():

	# Get base file to compare
	print(variable_list_messages[0])
	source_file_path = request_file_name()

	# Get file to compare agains base file
	print(variable_list_messages[1])
	error_file_path = request_file_name()

	# Process the two CSV to be compare
	csv_file_reader(source_file_path, error_file_path);

### Main
def main():
	# Welcome message
	message_id_matcher_welcome()

	interactive_menu()

	# Good bye message
	message_id_matcher_bye()
	
	# Close Colorama use
	deinit()

if __name__ == "__main__":
	main()
