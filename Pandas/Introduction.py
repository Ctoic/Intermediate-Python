''' Name : Najam Ali Abbas
    Date : 10/10/2019
    Purpose : To learm about Pandas and how to use it in data analysis 
    Topic : Pandas
'''
# pandas is a high level data manipulation tool developed by Wes McKinney
# it is built on the top of numpy package and its key data structure is called dataframe

# dictionary with country , capital , area and population

countries = { "Pakistan" : { "Capital" : "Islamabad" , "Area" : 881913 , "Population" : 220892340 },
                "India" : { "Capital" : "New Delhi" , "Area" : 3287263 , "Population" : 1311050527 },
                "Afghanistan" : { "Capital" : "Kabul" , "Area" : 652230 , "Population" : 38041754 },
                "China" : { "Capital" : "Beijing" , "Area" : 9596960 , "Population" : 1433783686 },
                "Japan" : { "Capital" : "Tokyo" , "Area" : 377835 , "Population" : 126476461 },
                "Russia" : { "Capital" : "Moscow" , "Area" : 17098242 , "Population" : 146599183 }
                }

import pandas as pa

# creating a dataframe from dictionary
# dataframe is a 2 dimensional data structure with labeled axes(rows and columns)
# dataframe is a tabular data structure


df = pa.DataFrame(countries)

# printing the dataframe

print(df)

# printing the index of dataframe

print(df.index)
