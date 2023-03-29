# genrating random data with numpy and matplotlib then finding the mean and standard deviation of the data

import numpy as np
import matplotlib.pyplot as plt

# generate random data

data = np.random.randn(1000)

# plot the data

plt.hist(data, bins=20)
plt.show()

# calculate the mean and standard deviation

mean = np.mean(data)
std = np.std(data)

print("Mean:", mean)
print("Standard deviation:", std)

# calculate the mean and standard deviation of the data

mean = np.mean(data)
std = np.std(data)

# generate random data

data = np.random.randn(1000) * std + mean

# plot the data

plt.hist(data, bins=20)
plt.show()

# calculate the mean and standard deviation of the data

mean = np.mean(data)
std = np.std(data)

print("Mean:", mean)

print("Standard deviation:", std)

