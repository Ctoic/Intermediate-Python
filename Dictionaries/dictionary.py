''' Author : Najam Ali Abbas 
    Date   : 10/10/2019
    Purpose: To learn about dictionaries in python
'''


# a dictionary containing countires and thier capitals

capitals  = { "Pakistan" : "Islamabad" , "India" : "New Delhi" , "Afghanistan" : "Kabul" }

# printing all the keys of dictionary

print ( capitals . keys ())

# printing all the values of dictionary

print ( capitals . values ())

# printing all the items of dictionary

print ( "Original Dictionary : " , capitals . items ())

# printing the value of key Pakistan

print ( capitals [ "Pakistan" ])

# adding a country to the list of capitals

capitals [ "China" ] = "Beijing"

# printing all the items again

print ( "Capitals after adding china " , capitals . items ())

# looping through the dictionary to print all the items

for  key , value  in  capitals . items ():
        print ( key ,":" ,  value )

# looping for keys only

for keys in capitals:
    print (keys)

# looping for values only

for values in capitals.values():
    print (values)

# adding 2 key value pairs to the dictionary

capitals.update({ "Japan" : "Tokyo" , "Russia" : "Moscow" })

# printing all the items again

print ( "Capitals after adding Japan and Russia " , capitals . items ())

# removing india from the list 

del capitals [ "India" ]

# printing all the items again

print ( "Capitals after removing India " , capitals . items ())

# printing all the countries with starting letter P

for keys in capitals:
    if keys.startswith("P"):
        print ("Countries starts with letter P :" , keys)

# printing all the countries with ending letter n
for keys in capitals:
    if keys.startswith("N"):
        print ("countries starts with letter n " , keys)
    else:
        print ("countries does not starts with letter n " , keys)
        


