

import pandas as pd

data = pd.read_csv("data.csv")

Q1 = data["MathScore"].quantile(0.25)
Q3 = data["MathScore"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = data[(data["MathScore"] < lower) | (data["MathScore"] > upper)] if not data[(data["MathScore"] < lower) | (data["MathScore"] > upper)].empty else "No outliers"

print("Lower limit:", lower)
print("Upper limit:", upper)
print("\nOutliers:")
print(outliers)
