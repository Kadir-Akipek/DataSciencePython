import numpy as np

dizi = np.linspace(0,10,5) #0 dan 10 a kadar 5 farklı sayı ver(sayılar sabit bir şekilde artar)
dizi

dizi1 = np.array(["a","b"])
dizi2 = np.array(["a","b"])
dizi3 = np.array([1,2])
dizi4 = np.array(["a",2])

dizi1 == dizi2
dizi1 == dizi3
dizi2 == dizi4

dizi2 != dizi4
dizi1 < dizi2