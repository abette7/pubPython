import pandas as pd
import openpyxl
import os
import shutil

xlsFile = (r'./Book1.xlsx')
myFolder = (r'./jpg')
outFolder = (r'./output')


df = pd.read_excel(xlsFile)
df.sort_values(by=['SKU'], ascending = True, inplace = True)
df.reset_index(drop = True, inplace = True)
print (df.head(3))

for dirpath, dirnames, filenames in os.walk(myFolder):
    for file_name in filenames:
        file_path = os.path.join(dirpath, file_name)
        print(file_name)
        myIndexPos = file_name.index('_')
        style_num = file_name[:myIndexPos]
        color_num = file_name[myIndexPos+1:-4]
        #print(style_num + ' ' + color_num)
        try:
            value = df.loc[(df['STYLE'] == style_num) & (df['COLOR'] == int(color_num)), 'SKU'].iloc[0]
            #print(value)
            newFile = f'{value}.jpg'
            newPath = os.path.join(outFolder,newFile)
            print(f'Copy {file_path} to {newPath}')
            shutil.copy(file_path, newPath)
        except:
            print(file_name + ' not found in xlsx.')
            