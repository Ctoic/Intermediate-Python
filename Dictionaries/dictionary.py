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

