import csv
import re

def csv_lowercase_az_first_word_to_txt(csv_file, column_index, output_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csv_input, open(output_file, 'w', encoding='utf-8') as txt_output:
        csv_reader = csv.reader(csv_input)
        
        # Skip the header if your CSV has one
        next(csv_reader, None)
        
        for row in csv_reader:
            if len(row) > column_index:
                # Extract only lowercase a-z from the first word
                first_word = row[column_index].split()[0] if row[column_index] else ''
                lowercase_az_only = re.sub(r'[^a-z]', '', first_word.lower())
                if lowercase_az_only:
                    txt_output.write(lowercase_az_only + '\n')

# Usage
csv_file_path = 'Indian-Male-Names.csv.csv'
column_to_extract = 0  # Change this to the index of the column you want (0, 1, or 2)
output_txt_file = 'output.txt'

csv_lowercase_az_first_word_to_txt(csv_file_path, column_to_extract, output_txt_file)
print(f"Lowercase a-z only first word from column {column_to_extract} has been extracted to {output_txt_file}")