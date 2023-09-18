import os
import sys
import csv
import shutil

directory = r"/Source"
outFolder = r'/Destination'
csvFile = (r'/PathToCSV/myCSV.csv')


for dirpath, dirnames, filenames in os.walk(directory):
    if 'Collateral' in dirpath:
        continue
    for file in filenames:
        if file.endswith('.jpg') and file.startswith('P-'):
            path = os.path.join(dirpath, file)
            myJobnum = file[2:8]
            #print(myJobnum)
            csv_reader = list(csv.reader(open(csvFile,'r')))
            for row in csv_reader:
                #print(row)
                oldJob = row[15]
                #print(f'{row[15]}, {myJobnum}')
                if oldJob[2:8] == myJobnum:
                    newFile = f'{row[7]}_{file}'
                    newPath = os.path.join(outFolder,newFile)
                    print(f'{path}, {newPath}')
                    shutil.copy(path,newPath)
