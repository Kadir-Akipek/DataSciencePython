import numpy as np
import pandas as pd 

liste = [1,2,3,4,5]

dizi = np.array(liste)
dizi

seri = pd.Series(liste) #seri = pd.Series(data, index)
seri

idx = ("A","B","C","D","E")
seri = pd.Series(data = liste, index = idx)
seri

sozluk = {"A":1, "B":2, "C":3, "D":4, "E":5}
seri2 = pd.Series(sozluk)
seri2


