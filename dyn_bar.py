import matplotlib.pyplot as plt

names = ['A', 'B', 'C', 'D', 'E']
values = []

for name in names:
    value = int(input(f'Enter value for {name}: '))
    values.append(value)

plt.bar(names, values)
plt.xlabel('Names')
plt.ylabel('Values')
plt.title('Dynamic Bar Chart')

plt.show()