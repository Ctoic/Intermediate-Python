import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('eng2.csv' , index_col = 0)

print(df)

# plotting given data on team names and goals scored 
 plt.plot(df['Team1'], df['FT'])