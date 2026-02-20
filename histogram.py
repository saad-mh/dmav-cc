import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4, edgecolor='black')
plt.title('Static Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()