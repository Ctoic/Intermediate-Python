import pandas as pd 

# creating a dataframe from dictionary 

data ={
    "Country" : ["Pakistan" , "India" , "Afghanistan" , "China" , "Japan" , "Russia"],
    "Capital" : ["Islamabad" , "New Delhi" , "Kabul" , "Beijing" , "Tokyo" , "Moscow"],
    "Area" : [881913 , 3287263 , 652230 , 9596960 , 377835 , 17098242],
    "Population" : [220892340 , 1311050527 , 38041754 , 1433783686 , 126476461 , 146599183]

}

another_data = {
    "Country" : ["Pakistan" , "India" , "Afghanistan" , "China" , "Japan" , "Russia"],
    "literacy_rate" : [50 , 60 , 70 , 80 , 90 , 100],
    "number_of_schools" : [100 , 200 , 300 , 400 , 500 , 600],
    "number_of_universities" : [10 , 20 , 30 , 40 , 50 , 60] , 
    "number_of_unemployed" : [1000 , 2000 , 3000 , 4000 , 5000 , 6000]


}

df = pd.DataFrame(data)
df.index = ["PK" , "IN" , "AF" , "CH" , "JP" , "RU"]
df2 = pd.DataFrame(another_data)
df2.index = ["PK" , "IN" , "AF" , "CH" , "JP" , "RU"]


# printing the dataframe

print(df)
print("=====================================================================================================")
print(df2)

