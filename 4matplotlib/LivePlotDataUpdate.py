import numpy as np
import matplotlib.pyplot as plt 


x = np.random.randint(80 , 180,50)
y = np.random.randint(80 , 180,50)
z = np.random.randint(80 , 180,50)
fig = plt.figure(figsize= (15,15))

X = []#Creat empty list
Y = []
Z = []
for index in range(x.shape[0]):
    axes = plt.axes(projection = '3d')
    X.append(x[index])#data will be append
    Y.append(y[index])
    Z.append(z[index])
    axes.scatter3D(X ,Y , Z)
    plt.pause(.5)#after .5 data will be update,pause after few tym
plt.show()