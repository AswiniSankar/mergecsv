# script to merge the CDR files and keep the merged file in the folder and moved the unmerged files into seperate folder

import os
import pandas as pd
from datetime import date
import shutil as st


source_folder = " " #give the source folder path 

os.chdir(source_folder)

if len(os.listdir(source_folder) ) == 0: 
	print('directory is empty')
	
else:
	today = date.today()
	#print("Today's date:", today)
	filename = "merged_" + str(date.today()) + '.csv'
	#print(filename)

	combined_csv = pd.DataFrame()

	combined_csv = pd.concat([pd.read_csv(f) for f in os.listdir(os.getcwd())])

	combined_csv.to_csv(filename, index=False, encoding='utf-8-sig')

	#destination path for the single files need to be give for future reference
	destination_folder = "" #give the desntination folder path

	for file in os.listdir(os.getcwd()):
	#check for the merged file name if present then it won't move the file
		if os.path.basename(file) == filename:
			continue
		
		else:
			source = file
			destination = destination_folder + file
			# move file
			st.move(source, destination)
			#print('Moved:', file)
	print('successfully merged the CDR files')
