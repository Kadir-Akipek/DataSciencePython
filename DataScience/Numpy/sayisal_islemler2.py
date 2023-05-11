import numpy as np

dizi = np.array([[1,2,3], 
                [4,5,6],
                [7,8,9]])

dizi.min() #dizideki minimum elemanı verir
dizi.max() #dizideki maximum elemanı verir

dizi.argmin() #bir fonksiyonun minimum noktası. Dizi nin minimum noktası

dizi.mean() #dizinin aritmetik ortalamasını verir
dizi.mean(axis=0) #her sütunun arimetik ortalamasını verir
dizi.mean(axis=1) #her satırın arimetik ortalamasını verir

dizi.std() #standart sapmayı verir
dizi.std(axis=0) #sütunlardaki standart sapmayı verir

dizi.var() #varyans hesaplar
dizi.var(axis=1) #satırlardaki varyansları hesaplar

dizi.clip(2,5) #sadece istenilen 2 değer arasındaki değerler kalır ve diğer değerleri yazdığımız aralıktaki değerlere dönüştürür

dizi2 = np.random.rand(3,3)*10
dizi2 = dizi2.round() #sayıları tamsayı olarak yuvarlar
dizi2

dizi3 = np.random.rand(3,3)*10
dizi3 = dizi3.round(decimals=2) #virgülden sonraki 2 sayıyı alır
dizi3