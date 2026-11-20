import pandas

data = pandas.read_csv("lifestyle_data.csv")

# What data type is `data` as output from the `read_csv()` method?
print(type(data))
# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
total_students = data.shape[0]
print(f"Total number of students: {total_students}")
# used the pandas.DataFrame.shape documentation to get the number of rows in the dataset, which corresponds to the total number of students.

# Find the mean average GPA of the students
mean_gpa = data["GPA"].mean()
print(f"Mean average GPA: {mean_gpa}")
# used the pandas.DataFrame.mean() documentation to calculate the mean of the 'GPA' column in the dataset.

# Find the standard deviation of how much sleep students get per day
std_dev_sleep = data["Sleep_Hours_Per_Day"].std()
print(f"Standard deviation of sleep hours per day: {std_dev_sleep}")
# used the pandas.DataFrame.std() documentation to calculate the standard deviation of the 'Sleep_Hours_Per_Day' column in the dataset.

# Find the maximum amount of study hours per day
max_study_hours = data["Study_Hours_Per_Day"].max()
print(f"Maximum study hours per day: {max_study_hours}")
# used the pandas.DataFrame.max() documentation to find the maximum value in the 'Study_Hours_Per_Day' column.

# Sort the students by social hours per day ascending (lowest -> highest)
sorted_by_social_hours = data.sort_values(by = "Social_Hours_Per_Day", ascending=True)
print(sorted_by_social_hours)
# used the pandas.DataFrame.sort_values() documentation to sort the dataset by the 'Social_Hours_Per_Day' column in ascending order.

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one
hour_columns = ["Study_Hours_Per_Day", "Extracurricular_Hours_Per_Day", "Sleep_Hours_Per_Day", "Social_Hours_Per_Day", "Physical_Activity_Hours_Per_Day"]

data["Total_hours"] = data[hour_columns].sum(axis=1, skipna=True, numeric_only=True, min_count=1)
print(data[["GPA", "Total_hours"]])
# used the pandas.DataFrame.sum() documentation to sum the values across the specified columns for each row, creating a new column 'Total_hours' in the dataset. 

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
high_stress_students = data[data["Stress_Level"] == "High"]
low_stress_students = data[data["Stress_Level"] == "Low"]
high_stress_mean_gpa = high_stress_students["GPA"].mean()
low_stress_mean_gpa = low_stress_students["GPA"].mean()


print(f"High stress students:{high_stress_students}")
print(f"Low stress students:{low_stress_students}")
print(f"Mean GPA of high stress students: {high_stress_mean_gpa}")
print(f"Mean GPA of low stress students: {low_stress_mean_gpa}")

# used DataFrame filtering to create two new DataFrames, one for high stress students and one for low stress students. Then calculated the mean GPA for each group using the mean() method on the 'GPA' column.
# Can you work out whether having a higher stress level leads to a higher GPA?

