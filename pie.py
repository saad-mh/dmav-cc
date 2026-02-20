import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 10]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

plt.show()