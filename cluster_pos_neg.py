import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(50)
y = -x + np.random.normal(0, 0.1, 50)
x = np.append(x, 0.2)
y = np.append(y, 2)

plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.title('Cluster of Positive and Negative Points')

plt.show()

# below is the manual code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
x = data['AttendanceRate']
y = data['MathScore']
x = np.append(x, 0.2)
y = np.append(y, 2)

plt.scatter(x, y)
plt.xlabel('Attendance Rate')
plt.ylabel('Math Score')

plt.title('Cluster of Positive and Negative Points')

plt.show()