# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
with open('student_data.csv', 'r') as f:
    data = f.readlines()

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3
averages = []
for row in data[1:]:
    columns = row.strip().split(',')
    id, name, maths, science, history = columns
    avg = (int(maths) + int(science) + int(history)) / 3
    averages.append((name, avg))

# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
with open('report.txt', 'w') as f:
    for name, avg in averages:
        f.write(f"{name}: {avg:.2f}\n")
