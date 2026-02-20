import matplotlib.pyplot as plt

names = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

plt.bar(names, values, color='blue', edgecolor='black')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()