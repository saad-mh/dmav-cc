import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker="o")

plt.xlabel("X - ind")
plt.ylabel("Y - d")

plt.title("X-Y Axis Data")

plt.grid(True)

plt.show()

