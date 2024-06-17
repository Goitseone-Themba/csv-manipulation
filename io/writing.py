import pandas as pd

data = {"Student Name": ["Mathew Davis", "Laura Martinez", "Charlotte Hall"], "Course": ["Software Engineering", "Applied Maths", "Environmental Science"],}

sheet = pd.DataFrame(data=data, columns=["Student Name", "Course"])

print(sheet.loc[[0, 1, 2]])



sheet.to_csv("Student_records.csv", index=False)