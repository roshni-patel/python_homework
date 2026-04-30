"""
Tasks 2-15
This will give errors to report what you need to fix.  You run it repeatedly as you create the following functions, until all functions are working correctly.
Remember to import the csv module for this task.

    Create a function called read_employees that has no arguments, and do the following within it.
        Declare an empty dict. You'll add the key/value pairs to that. Declare also an empty list to store the rows.
        You next read a csv file. Use a try block and a with statement, so that your code is robust and so that the file gets closed.
        Read ../csv/employees.csv using csv.reader(). (This csv file is used in a later lesson to populate a database.)
        As you loop through the rows, store the first row in the dict using the key "fields". These are the column headers.
        Add all the other rows (not the first) to your rows list.
        Add the list of rows (this is a list of lists) to the dict, using the key "rows".
        The function should return the dict.
        Add a line below the function that calls read_employees and stores the returned value in a global variable called employees. Then print out this value, to verify that the function works.
        In this case, it's not clear what to do if you get an exception. You might get an exception because the filename is bad, or because the file couldn't be parsed as a CSV file. For now, just use the same approach as described above: catch the exception, print out the information, and exit the program. 
        One likely exception in this case is an error in the syntax of your code.

    Run the test to see if you have this much right.

A word about what's going on when the test runs: The test file imports your assignment2.py module.  When the import statement occurs, all the program statements in your module that are outside of functions do run.  That means the statement which sets your employees global variable is run.  As a result, the assignment2-test.py can reference this global variable too -- and it does.  If you forget to set this variable in your program, the test reports an error.
"""


import csv
import traceback
import sys
import os
from datetime import datetime
import custom_module


def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            csv_reader = csv.reader(file)

            first_row = True
            for row in csv_reader:
                if first_row:
                    employees_dict["fields"] = row
                    first_row = False
                else:
                    rows.append(row)

            employees_dict["rows"] = rows
            return employees_dict

    except Exception as e:
       trace_back = traceback.extract_tb(e.__traceback__)
       stack_trace = list()
       for trace in trace_back:
          stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
       print(f"Exception type: {type(e).__name__}")
       message = str(e)
       if message:
          print(f"Exception message: {message}")
       print(f"Stack trace: {stack_trace}")
       sys.exit(1)


employees = read_employees()
print(employees)


def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")


def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]


def employee_find(employee_id):
    def employee_match(row):
       return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]


print(employees)


def employee_dict(employee_row):
    employee_data = {}

    for index in range(1, len(employees["fields"])):
        field_name = employees["fields"][index]
        employee_data[field_name] = employee_row[index]

    return employee_data


print(employee_dict(employees["rows"][0]))


def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees


print(all_employees_dict())


def get_this_value():
    return os.getenv("THISVALUE")


def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("test")
print(custom_module.secret)


def read_minutes():
    minutes1 = {"fields": [], "rows": []}
    minutes2 = {"fields": [], "rows": []}

    try:
        with open("../csv/minutes1.csv", "r") as file:
            csv_reader = csv.reader(file)

            first_row = True
            for row in csv_reader:
                if first_row:
                    minutes1["fields"] = row
                    first_row = False
                else:
                    minutes1["rows"].append(tuple(row))

        with open("../csv/minutes2.csv", "r") as file:
            csv_reader = csv.reader(file)

            first_row = True
            for row in csv_reader:
                if first_row:
                    minutes2["fields"] = row
                    first_row = False
                else:
                    minutes2["rows"].append(tuple(row))

        return minutes1, minutes2

    except Exception as e:
       trace_back = traceback.extract_tb(e.__traceback__)
       stack_trace = list()
       for trace in trace_back:
          stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
       print(f"Exception type: {type(e).__name__}")
       message = str(e)
       if message:
          print(f"Exception message: {message}")
       print(f"Stack trace: {stack_trace}")
       sys.exit(1)


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])
    minutes_set = minutes1_set.union(minutes2_set)
    return minutes_set


minutes_set = create_minutes_set()


def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list


minutes_list = create_minutes_list()
print(minutes_list)


def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda row: row[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_list))

    try:
        with open("./minutes.csv", "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(minutes1["fields"])
            csv_writer.writerows(converted_list)

        return converted_list

    except Exception as e:
       trace_back = traceback.extract_tb(e.__traceback__)
       stack_trace = list()
       for trace in trace_back:
          stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
       print(f"Exception type: {type(e).__name__}")
       message = str(e)
       if message:
          print(f"Exception message: {message}")
       print(f"Stack trace: {stack_trace}")
       sys.exit(1)


write_sorted_list()