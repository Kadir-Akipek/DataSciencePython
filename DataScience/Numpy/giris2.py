import numpy as np

liste = [1, 2, 3,"4"]
dizi = np.array(liste)

dizi.shape #4, dizinin satır ve sütun uzunluğunu verir
dizi.ndim #1, dizinin kaç boyutlu olduğunu verir

liste2 = ([1, 2], [3,4])
type(liste2)

dizi2 = np.array(liste2)
type(dizi2)
dizi2
dizi2.ndim #2
dizi2.shape #2

dizi2.fill(5) #tüm elemanları istediğimiz sayıya çeviririz
print(dizi2)