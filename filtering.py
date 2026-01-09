import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])
# print(productivity[productivity<8])
# # working hour between 5 to 7
# print(productivity[(productivity>=5)&(productivity<=8)])
# # print working hour of first employee withworking hour <8
# first_employee=productivity[:,0]
# print(first_employee)
# print(first_employee[first_employee<8])
# print last two working hr <7
last_two_employee=productivity[:,8:10]
print(last_two_employee)
print(last_two_employee[last_two_employee<7])
# <8=0
productivity[productivity<8]=0
print(productivity)