import numpy as np

# 2d numpy array

ara = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(ara)
print(ara[0, 0])
print(ara[0, 1])


for i in range(0, 3):
    for j in range(0, 3):
        print(ara[i, j], end=" ")
    print()


    # create a 3d numpy array

    print()

ara = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

for n in range(0 , 3):
    for i in range(0, 3):
        for j in range(0, 3):
            print(ara[n, i, j], end=" ")
        print()
    print()







