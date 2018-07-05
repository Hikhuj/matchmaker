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
import csv
import os
#import glob
#import sys
from colorama import *
init()

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
	print(result)
	return result


def request_file_A_path():

	print("Please provide the file that works as base document...")
	result = get_relative_path()
	return result


def request_file_B_path():

	print("Please provide the file that will be compare...")
	result = get_relative_path()
	return result


# Request compression of relative paths
def get_relative_path():

	# Variables
	result = ""
	absFilePath = ""

	print("")

	# Request the name of the file to work
	file_name = input("Copy and paste the file name to be used (use the format ==> fileName.extension): ")
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


def csv_file_reader(file_to_read_A, file_to_read_B):

	print("")

	with open(file_to_read_A, 'r', encoding='utf-8', newline='') as file_A:
		file_A = csv.reader(file_A, delimiter=',', quotechar=',')

		position = 1
		for row in file_A:
			# Restart always with clean array
			full_row = []
			print("=======> Processing line: " + str(position))
			full_row = search_id_in_file(row[0], file_to_read_B, position)
			row.extend(full_row)
			# row.append(full_row)
			# row.insert(7, full_row)
			write_on_file(row)

			# Increase row position
			position += 1


def search_id_in_file(line_id, file_to_read_B, position):

	result = []

	# Read the CSV where the code will pull data if it match in file_B
	with open(file_to_read_B, 'r', encoding='utf-8', newline='') as file_B:
		file_B = csv.reader(file_B, delimiter=',', quotechar=',')

		# Read each row of the CSV
		for row in file_B:
			if row[0] == line_id:
				result = row
				print(">>> Id found: " + str(position) + ", matching...")
				print(".")
				break

	return result


def write_on_file(row):

	with open ("clean.csv",'a') as clean_file:                            
		clean_file = csv.writer(clean_file, delimiter=',', quotechar=',')
		clean_file.writerow(row)


def interactive_menu():

	# Get base file to compare
	file_A_path = request_file_A_path()

	# Get file to compare agains base file
	file_B_path = request_file_B_path()

	# Process the two CSV to be compare
	csv_file_reader(file_A_path, file_B_path);

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