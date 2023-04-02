# create a list of population for afganistan , pakistan and india in Millions

population = [ 38041754 , 220892340 , 1311050527 ]

# create a list of countries

countries = [ "Afghanistan" , "Pakistan" , "India" ]

# Now how we can find what's population in pakistan with the help of countries list

# we can use index function to find the index of pakistan in countries list

# index function will return the index of pakistan in countries list

# we can use that index to find the population of pakistan in population list

index_pakistan  = countries . index ( "Pakistan" )

# now we can use that index to find the population of pakistan in population list

population_pakistan  = population [ index_pakistan ]

print ( "Population of Pakistan is :" ,population_pakistan )



# creating a dictionary of population of countries

population_dict  = { "Afghanistan" : 38041754 , "Pakistan" : 220892340 , "India" : 1311050527 }

# now we can find the population of pakistan with the help of key pakistan

population_pakistan  = population_dict [ "Pakistan" ]
