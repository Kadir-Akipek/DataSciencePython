import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(100,150,50) #(a,b,c) a:merkez
                                 #b:ölçek
                                 #c:sayı miktarı


x = x.round()
plt.hist(x,color="g")
plt.show()


