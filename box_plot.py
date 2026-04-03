import matplotlib.pyplot as plt

weights = [25, 28, 29, 30, 34, 35, 35, 37, 38]

plt.boxplot(weights)
plt.xlabel('Weights')
plt.title('Box Plot of Weights')
plt.show()

# Below is the manual code

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.boxplot(data['MathScore'])
plt.xlabel('Math Scores')
plt.title('Box Plot of Math Scores')
plt.show()