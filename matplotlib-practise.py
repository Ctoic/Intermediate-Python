import matplotlib.pyplot as plt
import numpy as np

# calculate the mean and standard deviation of the data
# standard deviation is the square root of the variance
# variance is the average of the squared differences from the mean
# what do standard deviation and variance tell us?
# standard deviation tells us how spread out the data is
# variance tells us how spread out the data is
# the higher the standard deviation and variance, the more spread out the data is
# the lower the standard deviation and variance, the less spread out the data is
# the mean is the average of the data
# the median is the middle value of the data
# the mode is the most common value of the data
# the range is the difference between the highest and lowest values of the data
# the interquartile range is the difference between the 75th percentile and the 25th percentile of the data
# the interquartile range is a measure of how spread out the middle 50% of the data is


courses = ["SDA" , "C-net" , "TBW" , "Digital-Mrkg", "Techno"]
expected_graduates = [ 100 , 80 , 85 , 95 , 95]

plt.bar(courses, expected_graduates)
plt.show()

# can we calculate the mean and standard deviation of the data?

mean = np.mean(expected_graduates)
std = np.std(expected_graduates)

print("Mean:", mean)
print("Standard deviation:", std)

# generate random data for the same courses for fifty students

data = np.random.randn(50) * std + mean

# plot the data

plt.hist(data, bins=20)
plt.show()

