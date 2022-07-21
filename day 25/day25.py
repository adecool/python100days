# with open('weather_data.csv') as weather_file:
#     data = weather_file.readlines()
#
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
# data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])
# data_dict = data.to_dict()
# print(data_dict)
#
# avg = data['temp'].mean()
# avg2 = data['temp'].max()
# print(avg2)
# # series to list
# data['temp'].to_list()
#
# # getting data in columns
# print(data['condition'])
#
# print(data.condition)


# print(temp_list)
# average = sum(temp_list)/len(temp_list)
# print(average)

#get data in row
#
# monday = data[data.day == 'Monday']
# def fahrenheit(temp):
#     convert = temp * 1.8 + 32
#     return convert
#
# print(fahrenheit(monday.temp))

#
# print(data[data.temp == data.temp.max()])

# create dataframe from scratch
# data_dict = {
#     'students' : ['any', 'james', 'angela'],
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
# red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])
#
# data_dict = {
#     'fur color': ['gray', 'red', 'black'],
#     'Count' : [gray_squirrel_count,red_squirrel_count,black_squirrel_count]
# }
# sq_data = pandas.DataFrame(data_dict)
# sq_data.to_csv('squirrel_count.csv')