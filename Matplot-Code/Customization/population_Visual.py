import matplotlib.pyplot as plt

# list of values for Revenue
Revenue = [ 100 , 80 , 85 , 95 , 95]

# list for years
years = [ 2010 , 2011 , 2012 , 2013 , 2014]

# plot the Revenue vs years
plt.plot(years, Revenue)

# label the x and y axis

plt.xlabel('Years')
plt.ylabel('Revenue')

# give a title to the graph

plt.title(label='Revenue vs Years', loc='center', pad=20, fontsize=20, color='green')

# plot yticks

plt.yticks([ 100 , 80 , 85 , 95 , 95], [ "100B" , "80B" , "85B" , "95B" , "95B"])

# adding Grids 
plt.grid(True)


# pyplot.show()

plt.show()
