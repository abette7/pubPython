from datetime import datetime, timedelta
from time import strftime, strptime
from xattr import xattr
import pandas as pd
import os.path
import time
import os
import openpyxl

directory = r'/Path to directory to generate a report from'
excelToExport = r'/Path to save xlsx doc'
file_data = []
for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        if file.endswith('.jpg') or file.endswith('.tif'):
            path = os.path.join(dirpath, file)
            date = os.path.getmtime(path)
            date = datetime.fromtimestamp(date)
            date = date.strftime('%Y-%m-%d %H:%M:%S')   
            name = os.path.basename(path) #.split('.')[0]
            #print(name)
            file_dict = dict()
            file_dict['Name'] = name
            file_dict['Date'] = date
            file_data.append(file_dict)
            #print(file_data)
            my_data = pd.DataFrame(file_data, columns=['Name', 'Date'])
            my_data.sort_values(by=['Name'], ascending=True, inplace=True)
            my_data['Date'] = pd.to_datetime(my_data['Date']).dt.date.astype('category')
            my_data = my_data.sort_values(by=['Name'], ascending=True)
            my_data = my_data.reset_index(drop=True)

initialize_columns = ['Name', 'Date']
try:
    my_data.head()
    my_data.to_excel(excelToExport, engine='openpyxl', index=False)
except:
    print('No jpg or tif Files Found')
