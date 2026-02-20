import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()
x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()

for i in range(1, 100):
    y1 = np.sin(x + i/10)
    y2 = np.cos(x + i/10)
    ax.clear()
    ax.plot(x, y1, label='sin(x)', color='blue')
    ax.plot(x, y2, label='cos(x)', color='orange')
    ax.set_title('Dynamic Sine and Cosine Functions')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.legend()
    plt.pause(0.1)

plt.ioff()
plt.show()