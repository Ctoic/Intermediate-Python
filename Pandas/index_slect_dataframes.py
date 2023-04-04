import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a Pandas dataframe from some data.
df = pd.read_csv('eng2.csv' , index_col=0)

# index_col=0 means that the first column of the csv file is the index column
 # index_col=1 means that the second column of the csv file is the index column
 # what's index column? it's the column that is used to identify the rows of the dataframe
    # in this case, the index column is the column that contains the names of the teams
    # so, the index column is the column that contains the names of the teams

sample_data = df["Team 1"]
sample_data2 = df[['Team 1']]
print(sample_data)
#pandas.core.series.Series is type of the below data 

print(type(sample_data))
print(sample_data2)
# print the type of the data
print(type(sample_data2))



