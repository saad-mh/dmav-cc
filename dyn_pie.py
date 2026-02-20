import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
vals = []

for label in labels:
    val = int(input(f'Enter value for {label}: '))
    vals.append(val)

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title('Dynamic Pie Chart')
plt.show()