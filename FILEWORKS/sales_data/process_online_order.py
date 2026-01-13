import numpy as np
data=np.loadtxt("FILEWORKS\\sales_data\\online_order.csv",delimiter=",",skiprows=1,dtype="str")
print (data)
# Shape of dataset
print("Dataset shape:", data.shape)
# Total number of orders
total_orders = data.shape[0]
print("Total orders:", total_orders)
# Extract UnitPrice column (index 4) and convert to float
unit_price = data[:, 4].astype("int")
average_unit_price = np.average(unit_price)
print(average_unit_price)
# Calculate total revenue per order
revenue_unit=(data[:,3].astype("int")*data[:,4].astype("int"))
print("revenue per order",revenue_unit)
# Find orders with delivery days > 5
print(data[data[:,6].astype("int") > 5])
