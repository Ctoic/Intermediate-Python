import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('eng2.csv' , index_col = 0)

print(df)

# Storing Team 1 names in a numpy array from the dataframe
team1 = df['Team 1'].values
print(team1)

# Now plotting them on a scatter plot 
plt.scatter(x = team1 , y = df['Team 2'].values ,  c = 'red' , alpha = 0.8)

# Previous customizations
plt.xscale('log')

plt.xlabel('Team 1')
plt.ylabel('Team 2')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()

