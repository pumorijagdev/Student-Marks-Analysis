import pandas as pd

df = pd.read_csv("Projects/PandasStudentMarkAnalysis/students.csv")

# avg marks for each subject
avg_marks = df.groupby("Subject")["Marks"].mean()
print("Average marks in each subject: ")
print(avg_marks)
print("---------------------------------------")

# find topper in each subject
print("Subject wise Topper: ")
print(df.loc[df.groupby("Subject")["Marks"].idxmax()])
print("---------------------------------------")

# calculate pass %
print("Passing percentage: ")
print((df[df["Marks"] >= 40].shape[0])/(df.shape[0]) * 100)
print("---------------------------------------")