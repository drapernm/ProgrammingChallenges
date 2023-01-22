'''
Author: Noah Draper
Brief Description: Program combines all CSV files in "fixtures" directory, excluding the combined file if it already exists.
                    New combined csv file will be in "fixtures"
References: https://medium.com/@stella96joshua/how-to-combine-multiple-csv-files-using-python-for-your-analysis-a88017c6ff9e
            https://stackoverflow.com/questions/41857659/python-pandas-add-filename-column-csv
            https://stackoverflow.com/questions/20638040/glob-exclude-pattern
'''
from generatefixtures import *
import os
from fileinput import filename
import pandas as pd
import glob
#set directory
os.chdir('fixtures')
# verify the path
#cwd = os.getcwd() 
#print("Current working directory is:", cwd)

#reference all CSV files in 'fixtures'
csv_files = glob.glob('[!_]*.csv')  #[!_] - excludes all files that start w/ underscore. name new file _combined_csv to avoid redundancies
#print(csv_files) #verify csv file list

data = [] #list of dataframes as an agrument

#csv basename in 'filename' column
for csv in csv_files:
    frame = pd.read_csv(csv)
    frame['filename'] = os.path.basename(csv) #put file basename in  filename column
    data.append(frame)

#create new csv file
combinedCSV = pd.concat(data, ignore_index=True) #create new csv file
print(combinedCSV) 

#export csv file to 'fixtures'
combinedCSV.to_csv('_combined_csv.csv', index=False, encoding='utf-8')
