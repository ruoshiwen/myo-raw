import numpy as np 

a = np.load('fist0.npy')
lenth = int(len(a)/8)
data = a.reshape(lenth,8)
print(a)