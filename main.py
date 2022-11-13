import furigana as furi
from datetime import datetime
import os

#variables for input data
source_folder = "source/"

#variables for output data
output_folder = "output/"
dt=datetime.now()
output_file = str(dt)+".txt"
output = output_folder+output_file

#Find and create list of needed definitions

for file in os.listdir(source_folder):
    source=source_folder+file
    input_list = furi.furigana(source) #add furigana to the words
    with open(output, 'a') as f: #write to separate file
        for each in input_list:
            f.writelines(each)
    #os.remove(source) #delete the input files