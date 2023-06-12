import csv
import pandas

# with open("weather_data.csv") as file:
#     data = file.readlines()
#     for d in range(len(data)):
#         data[d] = data[d].strip()
# print(data)

# with open("weather_data.csv") as data_file:
#     data = list(csv.reader(data_file))
#     temperature = []
#     print(data)
#     for row in data[1:]:
#         temp = int(row[1])
#         temperature.append(temp)
# print(temperature)

# import pandas
#
data = pandas.read_csv("weather_data.csv")
print(data)
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# print(data["temp"].max())
#
# Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in the rows
# print(data[data.temp == data.temp.max()])
# print(data.temp.max())
# tuesday = data[data.day == "Tuesday"]
# print(tuesday.temp)
#
#
# def celsius_to_fahr(temp_celsius):
#     temp_fahr = (temp_celsius * 9) / 5 + 32
#     return temp_fahr
#
#
# far = celsius_to_fahr(tuesday.temp)
# print(far)

# Create df from scratch

# data_dict = {
#     "students": ["Amy", "James", "Nick"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# squirrel_number = data["Primary Fur Color"].value_counts()
# # print(squirrel_number)
# squirrel_number = pandas.DataFrame(squirrel_number)
# # print(squirrel_number)
# squirrel_number.to_csv("squirrel_count.csv")

# pandas.DataFrame(squirrel_number)
# Loop through DF
# for(key, value) in squirrel_number.items():
#     print(value)

# LOOP THROUGH ROWS OF DF
# for(index, row) in data.iterrows():
#     print(row.day)

