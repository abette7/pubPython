### This script watches a folder for a file, then performs an action
### As-is this script check to see if the file is a complete image with PIL before performing a move command on the file

import os
import time
import shutil
from PIL import Image
import xattr
import warnings

def ignore_warnings():
   warnings.simplefilter(action='ignore', category=Image.DecompressionBombWarning)
   Image.MAX_IMAGE_PIXELS = None
   print("This might take a moment...\n")

ignore_warnings()

in_folder = "/In"
ot_folder = "/Out"

while True:
	# get a list of files in the folder
	files = os.listdir(in_folder)
	try:
		for file_name in files:
			file_path = os.path.join(in_folder, file_name)
			if os.path.isfile(file_path):
				with Image.open(file_path) as image:
					image.load()
					#image.show()
					#image.close() 
				new_name = "Part-" + file_name # add prefix to the filename
				new_file_path = os.path.join(ot_folder, new_name) # create the new path with the prefix
				shutil.move(file_path, new_file_path) # move the file to the new location
				time.sleep(1)
				
	except:
		print('Looping Until Pillow Opens Image')

print('Done!!!')

