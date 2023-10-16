student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic.iterrows()}
# for (index, row) in phonetic.iterrows():
#     phonetic_dict[row.letter] = row.code
print(phonetic_dict)

def generate_phonetic():
    user_input = list(input("Enter a word: ").upper())
    try:
        spelled = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
          print("Not Good")
          generate_phonetic()
    else:
         print(spelled)

generate_phonetic()
#
# # for (key, value) in phonetic_dict.items():
# #     if key in user_input:
# #         spelled.append(value)
# #
# # print(spelled)
# # for letter in user_input:
# #     if letter in phonetic_dict:
# #         spelled.append(phonetic_dict[letter])

