import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0,100,11) #(başlangıç,bitiş,eleman sayısı)
dizi1

dizi2 = dizi1**2
dizi2

plt.plot(dizi1,dizi2,"b--")
plt.show()

plt.plot(dizi1,dizi2,"g.-")
plt.show()
