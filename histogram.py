import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4, edgecolor='black')
plt.title('Static Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()

# Below is the manual code

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

plt.hist(data["MathScore"], bins=4, edgecolor='black')
plt.title('Static Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()