import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Static Line Plot')

plt.show()

# Below is the manual code

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

x = data["StudentID"]
y = data["MathScore"]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Math Scores of Students')

plt.xticks(rotation=90)

plt.show()