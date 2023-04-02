import matplotlib.pyplot as plt

lista = [1,2,3,4,5,6,7,8,9,10]
listb = ['a','b','c','d','e','f','g','h','i','j']

plt.plot(lista, listb)

# labeling the x and y axis

plt.xlabel('x-axis')
plt.ylabel('y-axis')

# giving a title to the graph
plt.title(label='My first graph', loc='center', pad=20, fontsize=20, color='red')

# plot yticks

plt.yticks([1,2,3,4,5,6,7,8,9,10], ['a','b','c','d','e','f','g','h','i','j'])




plt.show()

