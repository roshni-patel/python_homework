import csv

# Read CSV into list of lists
employees = []
with open("../csv/employees.csv", newline="") as file:
    reader = csv.reader(file)
    employees = list(reader)

# Skip header row
data_rows = employees[1:]

# List of full names: first_name + " " + last_name
names = [row[1] + " " + row[2] for row in data_rows]

print(names)

# Filter names containing the letter "e"
names_with_e = [name for name in names if "e" in name]

print(names_with_e)