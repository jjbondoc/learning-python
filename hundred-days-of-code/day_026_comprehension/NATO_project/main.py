student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv('./nato_phonetic_alphabet.csv') # read the CSV into a DataFrame

#iterrows() returns a Series for each row. The original columns of the DataFrame become the indexes for the Series
nato_dict = {nato['letter']: nato['code'] for (index, nato) in nato_df.iterrows()} # dict comprehension, accessing the different indexes of the Series
print(nato_df)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    name_input = input("What's your name?: ")
    
    #* Exception handling blocks
    try:
        nato_name = [nato_dict[letter.upper()] for letter in name_input] # access the nato_dict using each letter from the name_input
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_name)

generate_phonetic()