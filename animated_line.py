import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fig, ax = plt.subplots()
line, = ax.plot(x, np.zeros_like(x), 'b-')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
def update(num):
    line.set_ydata(np.sin(x + num / 10.0) * 5 + 5)
    return line,
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.title('Animated Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()