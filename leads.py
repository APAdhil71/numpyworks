import numpy as np
leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
    
])
# task 1 total leads generated each day
# print(np.sum(leads,axis=0))
# #task 2 total leads from each source
# print(np.sum(leads,axis=1))
# task 3 highest lead day
# daywise_total=np.sum(leads,axis=0)
# max_total=np.max(daywise_total)
# print(np.argmax(daywise_total))
# task 4 average leads per source
# print(np.average(leads,axis=1))
# # task 5 average leads per day
# print(np.average(leads,axis=0))
# task 6 highest lead  source
source_wise_total=np.sum(leads,axis=1)
max_total=np.max(source_wise_total)
print(np.argmax(max_total))