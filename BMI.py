"""
    Name : Najam Ali Abbas
    Date : 10/10/2019
    Purpose : Numpy and BMI
    Topic : Numpy
    
 """

import numpy as np

# Define arrays for weight and height
weight = np.array([50, 60, 70, 80, 90])
height = np.array([1.6, 1.7, 1.8, 1.9, 2.0])

# Calculate body mass index (BMI)
bmi = weight / height ** 2

# Print BMI values
print("BMI values:", bmi)

for i in range(0, 5):
    print("BMI value", i, "is", bmi[i])

# print bmi values less than 25
print("BMI values less than 25:", bmi[bmi < 25])


# print bmi values greater than 25

print("BMI values greater than 25:", bmi[bmi > 25])

# print bmi values less than 25 and greater than 20

print("BMI values less than 25 and greater than 20:", bmi[(bmi < 25) & (bmi > 20)])
