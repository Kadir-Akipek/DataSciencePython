import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
data

data.shape #43 satır 6 sütun var
data.isnull() #veri setimizde NULL değer olup olmadığına bakıyoruz
data.isnull().sum() #bu da başka bi yolu



#bar grafiği oluşturacağız
x = data["OrderDate"]
y = data["Unit Price"]
plt.figure(figsize = (15,8)) #grafiğin boyutunu büyültmek için figür oluşturacağız
plt.bar(x,y)
plt.show()

#bar grafiğimi özelleştirdim
x = range(1,44)
y = data["Unit Price"]
plt.figure(figsize = (15,8))
plt.bar(x,y, color = "purple", width = 0.5)
plt.xlabel("Günler")
plt.ylabel("Birim Fiyat")
plt.title("Satışlar")
plt.xticks(np.arange(1,44,1)) #1 den başladık ve 43 de bitirdik
plt.show()

#bar grafiğine çizgi grafiği ekledim
x = range(1,44)
y = data["Unit Price"]
plt.figure(figsize = (15,8))
plt.bar(x,y, color = "purple", width = 0.5)
plt.xlabel("Günler")
plt.ylabel("Birim Fiyat")
plt.title("Satışlar")
plt.xticks(np.arange(1,44,1))
plt.plot(x,y, color = "cyan")
plt.legend(labels = ["Satışlar"])
plt.show()

#ilk analizim
satislar = data.groupby("Item") #veri setimizde olan Item lara göre gruplandırma yapacağım
satislar = satislar.sum() #grafiğin özetini aldık
satislar = satislar.plot()
plt.show()

satislar = data.groupby("Item") 
satislar = satislar.sum() 
satislar = satislar.plot(kind = "bar") #grafiğin türünü barr yaptım
satislar.set_ylabel("Miktar & Birim Fiyat")
plt.show()

