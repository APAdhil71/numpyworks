import numpy as np 
data=np.loadtxt("FILEWORKS\\sales_data\\sales.csv",delimiter=",",skiprows=1,dtype="str")
print(data)
unit_sold=data[:,3].astype("int")
# print(np.sum(unit_sold),"total units sold")
# max_unit=data[:,3].astype("int")
# # print(np.max(unit_sold),"max_sold_unit")
# min_unit=data[:,3].astype("int")
# # print(np.min(unit_sold),"min_sold_unit")
# avg_unit=data[:,3].astype("int")
# print(np.average(unit_sold),"= average_sold_unit ")
revenue_unit=(data[:,3].astype("int"))*data[:,4].astype("float")
# print(revenue_unit)
sum_revenue_unit=np.sum(revenue_unit)
print(sum_revenue_unit)
# units sold >8
# print(data[data[:,3].astype("int")>8])
# # category == electronics
# print("electronics",data[data[:,2]=="Electronics"])

# flat 100 for all products
# data[:,4]=data[:,4].astype("int")-100
# print(data,"discount")
north_region=data[data[:,-1]=="North"]
print(north_region)
total_revenue_north=(north_region[:,-3].astype("int"))*north_region[:,-2].astype("int")
print(total_revenue_north)
print(np.sum(total_revenue_north))