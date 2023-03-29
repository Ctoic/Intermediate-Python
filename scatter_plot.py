import numpy as np
import matplotlib.pyplot as plt

# generate random data for scatter plot

data_x= np.random.randn(10)

data_y = np.random.randn(10)


# plot the data on scatter plot

plt.scatter(data_x, data_y)
plt.show()

# plot the data with piechart 

plt.pie(data_x)
plt.show()

