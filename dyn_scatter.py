import matplotlib.pyplot as plt

n = int(input("Enter the number of data points: "))
x, y = [], []

for i in range(n):
    x_val = float(input(f"Enter x value for point {i+1}: "))
    y_val = float(input(f"Enter y value for point {i+1}: "))
    x.append(x_val)
    y.append(y_val)

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Dynamic Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()