import numpy as np
data=np.genfromtxt("FILEWORKS\\titanic_case_study\\titanic.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
print("total",data.shape)
# total number survial
alive=data[data[:,1].astype('int')==1]
# print("alive",alive.shape)
# total number of death
death=data[data[:,1].astype('int')==0]
# print("death",death.shape)
# survival analysis
# survived rate
survived_unsurvived=data[:,1].astype('int')
# survived=survived_unsurvived[survived_unsurvived==1]
# print(f"total number of  survived{survived.size}")
# survival_rate=(survived.size/survived_unsurvived.size)*100
# print(survival_rate)
# death
# death=survived_unsurvived[survived_unsurvived.size==0]
# print(death.size)
# death_rate=(death/survived_unsurvived.size)*100
# print(death_rate)
# gender analysis
# total number of males 
# total number of females
# males survial rate
# female survial rate
# genders=data[:,3]
# male_count=genders[genders=="male"].size
# print(male_count)
# female_count=genders[genders=="female"].size
# print(female_count)
# survived_males=data[(data[:,3]=="male")&(data[:,1].astype("int")==1)]
# survived_male_count=survived_males[:,0].size
# print(f"survival rate {survived_males}")
# male_survival_rate =(survived_male_count/male_count)*100
# print(f"male survival rate {male_survival_rate}")
# # filter survived females
# survived_females = data[(data[:, 3] == "female") & (data[:, 1].astype(int) == 1)]
# # count survived females
# survived_female_count = survived_females[:,0].size
# print(f"survived females count: {survived_female_count}")
# # female survival rate
# female_survival_rate = (survived_female_count / female_count) * 100
# print(f"female survival rate: {female_survival_rate}")
# # age analysis
ages=data[:,4].astype("int")
print(f"min age {np.min(ages)}")
print(f"max age {np.max(ages)}")
print(f"avg age {np.average(ages)}")
# fare analysis
fare=data[:,-2].astype("float")
print(f"min fare {np.min(fare)}")
print(f"max fare {np.max(fare)}")
print(f"avg fare {np.average(fare)}")
# sort
print(data[np.argsort(data[:,-2].astype("float"))])

