import matplotlib.pyplot as plt

courses = ["SDA" , "C-net" , "TBW" , "Digital-Mrkg", "Techno"]
expected_graduates = [ 100 , 80 , 85 , 95 , 95]

plt.bar(courses, expected_graduates)
plt.show()