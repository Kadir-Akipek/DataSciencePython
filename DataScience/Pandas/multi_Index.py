import  pandas as pd
import numpy as np

idx1 = ["A","A","A","B","B","B"]
idx2 = ["a","b","c","d","e","f"]

idx_m = list(zip(idx1, idx2))
idx_m

idx_m = pd.MultiIndex.from_tuples(idx_m)
idx_m

liste = [[1,10],[2,20],[3,30],[4,40],[5,50],[6,60]]
dizi = np.array(liste)

tablo = pd.DataFrame(dizi, index = idx_m, columns = ["x","10x"])
tablo

tablo = tablo.loc["A"].loc["b"]
tablo