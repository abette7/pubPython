import os
import shutil
import re

### This script uses brackets as placeholder characters.
### If your file names use brackets select another pair of place
### holder characters for the three newFile_name assignments below  

myFolder = (r'/Users/adam.betterton/Desktop/untitled folder 8')
startPattern = '_('
endPattern = '_m'

for dirpath, dirnames, filenames in os.walk(myFolder):
    for file_name in filenames:
        file_path = os.path.join(dirpath, file_name)
        #print(file_name)
        newFile_name = file_name.replace(startPattern, '[')
        newFile_name = newFile_name.replace(endPattern, ']')
        newFile_name = re.sub(r'\[.*?\]', '', newFile_name)
        #print(newFile_name)
        newFile_path = os.path.join(dirpath, newFile_name)
        shutil.move(file_path, newFile_path)
