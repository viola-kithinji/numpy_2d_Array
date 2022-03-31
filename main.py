import numpy as np
height=[30,23,45,67,78]
weight=[56,78,89,90,67,]
np_height=np.array(height)
np_weight=np.array(weight)
print(weight)
bmi=np_weight/np_height**2
print(bmi)
np_2d=np.array([height,weight])
print(np_2d)
