import numpy as np

marks = np.array([
    [43, 42, 45, 34, 23],  # vipin
    [23, 45, 45, 34, 37],  # hari
    [37, 38, 39, 40, 45]   # cibin
])
# Display marks of Hari
print(marks[1])
#display Maths mark of hari
print(marks[1,0])
#display all students marks of Malayalam
print(marks[:,2])
# Display Malayalam and CS marks of all students
print(marks[:,2:4])
# Display English and Malayalam marks of Hari and Cibin
print(marks[1:3, 1:3])
