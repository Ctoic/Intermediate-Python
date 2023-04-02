import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars

cars.index = row_labels



# Print cars again

print(cars) 

# Import pandas as pd

# Import the cars.csv data: cars

cars = pd.read_csv('cars.csv')

# adding Index_col = 0 to read the first column as index

cars = pd.read_csv('cars.csv', index_col = 0) 

# Print out cars

print(cars)