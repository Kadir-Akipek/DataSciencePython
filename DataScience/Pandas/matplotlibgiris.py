import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veri1 = range(10)
veri2 = np.linspace(1,10,10) #(A,B,C) => A: Başlangıç
                             #(A,B,C) => B: Bitiş
                             #(A,B,C) => C: Sayı miktarı

#grafik oluşturma
plt.plot(veri1,veri2)
plt.show()

veri2 = veri2**2

plt.plot(veri1,veri2,"red")
plt.show()