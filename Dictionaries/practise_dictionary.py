# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data

data = {'capital':'rome', 'population':59.83}


# Add data to europe under key 'italy'

europe['italy'] = data


# Print europe

print(europe)



print(europe['norway']['capital'])

# printing the population aof all countries 

for keys in europe:
    print (europe[keys]['population'])


