# new_list = [n*2 for n in range(1, 5)]
# new_list = [n*2 for n in range(1, 5) if n > 3]
# names = ["Sabrina", "Ionela", "Oana", "Nicolae", "Nikc", "Ion"]
# short_name = [name for name in names if len(names) < 5]
# short_name = [name for name in names if len(name) < 5]
# cap_names = [name.upper() for name in names if len(name) >=5 ]

import pandas
# Open 2 text file and create a list that contains common values in each
with open("file1.txt") as data1:
    file_text1 = data1.readlines()
    # print(file_text1)

with open("file2.txt") as data2:
    file_text2 = data2.readlines()
    # print(file_text2)

results = [int(num.strip()) for num in file_text1 if num in file_text2]
print(results)

