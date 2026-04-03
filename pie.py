import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 10]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

plt.show()

# Below is the manual code

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")

labels = ["Maths","Physics","Chemistry","Programming"]
tmp_vals = data["MathScore"].mean(), data["PhysicsScore"].mean(), data["ChemistryScore"].mean(), data["ProgrammingScore"].mean()
values = tmp_vals

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Mean Score Distribution')

plt.show()