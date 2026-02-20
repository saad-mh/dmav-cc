import matplotlib.pyplot as plt

n = int(input("Enter the number of data points: "))
data = []

for i in range(n):
    value = float(input(f"Enter value for data point {i + 1}: "))
    data.append(value)

plt.hist(data, bins=10, edgecolor='black')
plt.title('Dynamic Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()