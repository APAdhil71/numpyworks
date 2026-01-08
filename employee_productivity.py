import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])

# 1. Calculate the total number of hours worked by each employee over 10 days
total_hours_employee = np.sum(productivity, axis=1)
print(total_hours_employee)
# 2. Calculate the total work hours for each day across all employees
total_hours_day = np.sum(productivity, axis=0)
print(total_hours_day)
# 5. Identify the employee index who worked the maximum total hours
max_employee_index = np.argmax(total_hours_employee)
print(max_employee_index)
# 6. Identify the employee index who worked the minimum total hours
min_employee_index = np.argmin(total_hours_employee)
print(min_employee_index)
# 7. Find the day index with the highest total working hours
max_day_index = np.argmax(total_hours_day)
print(max_day_index)
# 9. Calculate the difference between the most productive and least productive employee
productivity_difference = np.max(total_hours_employee) - np.min(total_hours_employee)


