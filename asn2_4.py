#!/usr/bin/env python 
import csv
import shutil
import logging
import sys
import getopt


class Logger(object):
	def __init__(self, filename="log_file.log"):
     	  	self.terminal = sys.stdout
     		self.log = open(filename, "a")
	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

sys.stdout = Logger("log_file.log")


print "\nOutput Displayed !" 

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('log_file.log')
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)

logger.info('Executed file')

ReadData=["COMPANY,Share Value,Status".split(",")]

def reader(file_obj):
	reader = csv.DictReader(file_obj, delimiter=',')
	
	for line in reader:
		
		ReadData.append([line["COMPANY"],line["Share Value"],line["Status"]])
		print(line["COMPANY"]),
		print(line["Share Value"]),
		print(line["Status"])
if __name__ == "__main__":
	with open("output.csv") as f_obj:
		reader(f_obj)
		

def csv_writer(data, path):
	with open(path, "wb") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		for line in data:
			writer.writerow(line)

if __name__ == "__main__":
	Cmpy = raw_input("Enter the Company Name:")
	shar = input("Enter the Share Value:")
	status=raw_input("Enter the Status:")

	'''data = ["COMPANY,Share Value,Status".split(","),
	
		"Facebook,70.42,none".split(","),
		"Apple,480.36,none".split(","),
		[Cmpy,shar,status]
		]'''
	ReadData.append([Cmpy,shar,status])	
	
	newdata = ReadData
	
	path = "output.csv"
	csv_writer(ReadData, path)


def reader(file_obj):
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		print(line["COMPANY"]),
		print(line["Share Value"]),
		print(line["Status"])
if __name__ == "__main__":
	with open("output.csv") as f_obj:
		reader(f_obj)


change_rates = {}
selected = 1
selected=int(raw_input("Please select an option: (1 to change, 0 to exit)"))
if selected == 1:
	change = raw_input("\nWhich Company Share Value would you like to change?: ")
	changeRt = float(raw_input("\nWhat would you like to change the rate to: "))
		
	change_rates[change] = changeRt
	newvalue = changeRt


if len(change_rates) > 0:
	with open('output.csv', 'r') as f_in,\
		open('output.csv.tmp', 'w') as f_out:
		exchReader = csv.reader(f_in)
		exchWriter = csv.writer(f_out)
		#prevalue= change_rates[change]
		for row in exchReader:
			if row[0] in change_rates:
				row[1] = change_rates[row[0]]
			exchWriter.writerow(row)
	shutil.move('output.csv.tmp', 'output.csv')


if len(change_rates) > 0:
	prevalue = change_rates[change]
	for row in newdata:
		if row[0] in newdata:
			row[1] = newdata[row[0]]
	prevalue=row[1]

if prevalue < newvalue:
	x="up"
else:
	if prevalue > newvalue:
		x="down"
	else:
		x="none"

if len(change_rates) > 0:
	with open('output.csv', 'r') as f_in,\
		open('output.csv.tmp', 'w') as f_out:
		exchReader = csv.reader(f_in)
		exchWriter = csv.writer(f_out)
		#prevalue= change_rates[change]
		for row in exchReader:
			if row[0] in change_rates:
				row[2] = x
			exchWriter.writerow(row)
	shutil.move('output.csv.tmp', 'output.csv')



def reader(file_obj):
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		
		print(line["COMPANY"]),
		print(line["Share Value"]),
		print(line["Status"])
if __name__ == "__main__":
	with open("output.csv") as f_obj:
		reader(f_obj)
