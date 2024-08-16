# Using just file methods
with open("./weather_data.csv", "r") as data_file:
    data = data_file.readlines()
    print("\n#Using just file methods")
    print(data)

# Using csv library
import csv

with open("./weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    temp = []

    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))

    print("\n#Using csv library")
    print(temp)

# Using the pandas library
import pandas

data = pandas.read_csv("./weather_data.csv")
print("\n#Using the pandas library")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp.iloc[0])
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)

data_dict = {
    "students": ["Amy", "James", "Angela", "Ahmed", "Hussein"],
    "scores": [12, 34, 56, 78, 90]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

# Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print("\n#Central Park Squirrel Data Analysis")
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("Squirrel_Data.csv")
