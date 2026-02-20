import matplotlib.pyplot as plt

n = int(input("Enter the number of data points: "))

x, y = [], []

for i in range(n):
    xi = float(input(f"Enter x[{i}]: "))
    yi = float(input(f"Enter y[{i}]: "))
    x.append(xi)
    y.append(yi)

plt.plot(x, y, marker='o')
plt.title('Dynamic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()