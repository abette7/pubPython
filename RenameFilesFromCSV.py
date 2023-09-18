## import csv to read to list.
import csv
import os
import shutil


##Main List path
myCSV = r'/Users/adam.betterton/Desktop/untitled folder 5/Book1.csv'
myFolder = r'/Volumes/Creative_2023/HardSurface/Collateral'
myOutput = r'/Users/adam.betterton/Desktop/Collect'

CSV_reader = list(csv.reader(open(myCSV, 'r')))

for row in CSV_reader:
	matchName = f'{row[0]}'
	#print(matchName)
	files = os.listdir(myFolder)
	for file_name in files:
		file_path = os.path.join(myFolder, file_name)
		#myIndex = file_name.find('_')
		myChunk = file_name[:8]
		#print(myChunk)
		if myChunk == matchName:
			newFileName = f'{file_name}'
			print(f'Match! {file_name} rename to {newFileName}')
			newFilePath = os.path.join(myOutput, newFileName)
			shutil.copy(file_path, newFilePath)
