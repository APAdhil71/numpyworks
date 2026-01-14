# Q1 load the csv
import numpy as np
data=np.genfromtxt("FILEWORKS\\ipl\\ipl.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
print(data)
#Q2 Total number of matches
total_matches = data.shape[0]
print(total_matches)
# 3. Matches played in 2023
matches_2023 = data[data[:,1].astype("int") == 2023]
print(matches_2023)
# 4. Max & Min runs by team_1
print(np.max(data[:,5].astype("int")))
print(np.min(data[:,5].astype("int")))