import pandas as pd

# # data = pd.read_csv("weather_data.csv")
#
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # print((monday.temp[0] * 1.8)+32)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_file")
# print(data)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240110.csv")

grey_squirell_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squirell_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirell_count = len(data[data['Primary Fur Color'] == "Black"])

print(grey_squirell_count)

dict_of_squireels = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirell_count, red_squirell_count, black_squirell_count]
}

data_to_csv = pd.DataFrame(dict_of_squireels)
data_to_csv.to_csv("squirell count")