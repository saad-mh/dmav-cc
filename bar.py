import matplotlib.pyplot as plt

names = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

plt.bar(names, values, color='blue', edgecolor='black')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()

# Below is the manual code


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

students = data["StudentID"]
math_scores = data["MathScore"]

plt.figure()
plt.bar(students, math_scores)

plt.xlabel("Student ID")
plt.ylabel("Math Score")
plt.title("Math Scores of Students")

plt.xticks(rotation=90)

plt.show()

"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

subjects = ["MathScore","PhysicsScore","ChemistryScore","ProgrammingScore"]
avg_scores = data[subjects].mean()

plt.figure()
plt.bar(subjects, avg_scores)

plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.title("Average Score per Subject")

plt.show()
"""