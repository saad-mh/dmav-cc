import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
circle = Circle((0, 5), 0.5)
ax.add_patch(circle)

def init():
    circle.center = (0, 5)
    return circle,

def animate(i):
    x = i * 0.1
    circle.center = (x, 5)
    return circle,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)
plt.show()