import numpy as np
import matplotlib.pyplot as plt

liste1 = [10,15,20,25,30,35,40,45,50]
liste2 = [330,270,85,60,530,15,750,305,320]

arr1 = np.array(liste1)
arr2 = np.array(liste2)

plt.plot(arr1,arr2,"g")
plt.title("Bu Grafiğin Başlığı")
plt.xlabel("X Verisi")
plt.ylabel("Y Verisi")
plt.show()