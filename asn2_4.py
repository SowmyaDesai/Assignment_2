import csv
import shutil
def csv_writer(data, path):
	with open(path, "wb") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		for line in data:
			writer.writerow(line)

if __name__ == "__main__":
	data = ["COMPANY,Share Value".split(","),
		"Google,123.45".split(","),
		"Facebook,70.42".split(","),
		"Apple,480.36".split(",")
		]
	path = "output.csv"
	csv_writer(data, path)



def reader(file_obj):
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		print(line["COMPANY"]),
		print(line["Share Value"])
if __name__ == "__main__":
	with open("output.csv") as f_obj:
		reader(f_obj)


change_rates = {}
selected = 1
while selected:
   	
    selected=int(raw_input("Please select an option: (1 to change, 0 to exit)"))
    if selected == 1:
    
        change = raw_input("Which Company Share Value would you like to change?: ")
        changeRt = float(raw_input("What would you like to change the rate to: "))
        change_rates[change] =  changeRt
	

if len(change_rates) > 0:
    with open('output.csv', 'r') as f_in,\
        open('output.csv.tmp', 'w') as f_out:
        exchReader = csv.reader(f_in)
        exchWriter = csv.writer(f_out)
        for row in exchReader:
            if row[0] in change_rates:
                row[1] = change_rates[row[0]]
            exchWriter.writerow(row)
    shutil.move('output.csv.tmp', 'output.csv')


def reader(file_obj):
	reader = csv.DictReader(file_obj, delimiter=',')
	for line in reader:
		print(line["COMPANY"]),
		print(line["Share Value"])
if __name__ == "__main__":
	with open("output.csv") as f_obj:
		reader(f_obj)




