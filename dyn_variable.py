import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

x = []
y = []

for i in range(n):
    xi = float(input(f"Enter x{i+1}: "))
    # yi = float(input(f"Enter y{i+1}: "))
    x.append(xi)
    # y.append(yi)


def f(x):
    return 2**x

y = [f(xi) for xi in x]

plt.plot(x, y, marker="o")

plt.xlabel("X - ind")
plt.ylabel("Y - d")
plt.title("X-Y Axis Data")

plt.grid(True)
plt.show()