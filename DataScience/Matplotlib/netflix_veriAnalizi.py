import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("netflix.csv")
data.shape #datamız 7787 satır ve 5 sütundan oluşuyormuş
data.info
data.isnull().sum()

data["country"] #country kolonunda hangi ülkelerin olduğuna bakıyoruz
data["country"].count() #7200 tane country varmış

ulkeler = data["country"].value_counts() #hangi ülkelerin ne kadar netflix yapımına sahip olduğunu verecek
ulkeler.head(20) #ilk 20 veriyi gösterir
ulkeler = pd.DataFrame({"Yapım Sayısı": data["country"].value_counts()})
ulkeler

#yapım sayısın veren grafikler
x = ulkeler.index 
x = x[0:12]

y = ulkeler["Yapım Sayısı"]
y = y[0:12]

plt.figure(figsize = (15,8))
plt.bar(x,y)
plt.title("En çok netflix yapımına sahip olan 12 ülke")
plt.show()

plt.figure(figsize = (15,8))
x = x[2:12]
y = y[2:12]
renk = ["cyan","cyan","cyan","cyan","cyan","cyan","cyan","red","cyan","cyan"]
plt.bar(x, y, color = renk)
plt.title("En çok netflix yapımına sahip olan 12 ülke")
plt.show()

#yerli yapımlara göz atalım
yerli1 = data.loc[data["country"]=="Turkey"] #country sütununda Turkey e eşit olan verileri takibe al
yerli1

yerli2 = yerli1["director"].value_counts()
yerli2

yonetmen = data.loc[data["director"]=="Yılmaz Erdoğan"] #Yılmaz Erdoğan ın yönettiği filmleri listeledik
yonetmen

director = data["director"].value_counts() #her bir yönetmenin kaç tane filmi olduğunu hesaplayacağız
director = pd.DataFrame({"Yapım Sayısı" : data["director"].value_counts()})
director

