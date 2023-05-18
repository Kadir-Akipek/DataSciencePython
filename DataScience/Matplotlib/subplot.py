import matplotlib.pyplot as plt

#plt.subplot(2,1,1) soldaki2 (grafiği yatay olarak 2 parçaya böler)
#plt.subplot(1,2,1) ortadaki1 (grafiği dikey olarak 2 parçaya böler)

dizi1 = range(10)
dizi2 = range(5,15)

plt.subplot(1,2,1)
plt.plot(dizi1,dizi2, "b.-")
plt.subplot(1,2,2) #sağdaki 2 (bana 2 grafik oluştur)
plt.plot(dizi2,dizi1, "r--")
plt.show()


