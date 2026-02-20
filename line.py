import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Static Line Plot')

plt.show()