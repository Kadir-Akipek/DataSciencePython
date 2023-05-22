import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(15,10)*100 #matris oluşturduk
y = np.random.randn(15,10)*100
plt.scatter(x,y)
plt.show()

x = np.random.rand(15,10)*100 #matris oluşturduk
y = np.random.randn(15,10)*100
plt.scatter(x,y,color="black")

z = np.random.rand(15,10)*100 #matris oluşturduk
t = np.random.randn(15,10)*100
plt.scatter(z,t,color="r")
plt.show()

x = np.random.rand(15,10)*100 #matris oluşturduk
y = np.random.randn(15,10)*100
plt.scatter(x,y,color="black", alpha=0.5)

z = np.random.rand(15,10)*100 #matris oluşturduk
t = np.random.randn(15,10)*100
plt.scatter(z,t,color="r",alpha=0.5)
plt.show()

arr1 = np.array([1,2,3,5,7])
arr2 = np.array([10,20,30,40,50])
renk = ["black","red","pink","blue","green"]
boyut = [100,250,500,1000,2000]

plt.scatter(arr1,arr2,color=renk,s = boyut)
plt.colorbar()
plt.show()













