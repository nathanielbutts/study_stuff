# Intended to use with text_to_anki
# This will create the necessary ruby tags for furigana
# Find the tags in each sentence, replace with ruby tags, save the file
import re

def add_readings():
    return None

def furigana(source):
    with open(source, 'r') as f:
        output_list = []
        input_list = []
        input_list = [line.rstrip() for line in f] #Creates list of all sentences, removes \n
        for line in input_list:
            z = re.sub("\]", "</rt></ruby>",line)
            x = re.sub("\[", "<ruby>", z)
            y = re.sub("\|", "<rt>", x)
            output_list.append(y)
    return output_list

def create_definitions(source):
    with open(source, 'r') as f:
        output_list = []
        input_list = []
        input_list = [line.rstrip() for line in f] #Creates list of all sentences, removes \n
        #for line in input_list:
