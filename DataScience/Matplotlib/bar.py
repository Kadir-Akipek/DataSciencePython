import matplotlib.pyplot as plt
import numpy as np

liste1 = ["X","Y","Z","T"] 
liste2 = [10,20,15,5] 
plt.bar(liste1, liste2)
plt.show()

liste1 = ["X","Y","Z","T"] 
liste2 = [10,20,15,5] 
plt.bar(liste1, liste2, color = "purple", width = 0.2) #garfiği özelleştirdik
plt.show()


liste1 = ["X","Y","Z","T"] 
liste2 = [10,20,15,5] 
plt.barh(liste1, liste2, color = "red", height = 0.2) #grafiği yatay hale getirdik
plt.show()

liste3 = [40,35,27,12]
liste4 = [10,20,15,5]
x = np.arange(4) #or x = ["X","Y","Z","T"]

plt.bar(x, liste3, color = "red",width = 0.2)
plt.bar(x, liste4, color = "purple",width = 0.2)
plt.title("Başlık")
plt.xlabel("Yatay Eksen")
plt.ylabel("Düşey Eksen")
plt.xticks(x, ("X","Y","Z","T")) #x eksenine eklemeler yaptım
plt.legend(labels = ["Kırmızı","Mor"])
plt.show()
