import pandas as pd
import numpy as np

sozluk = {"Fakülte":["Makine M.","Makine M.","Endüstri M.",
                     "Endüstri M.","Mekatronik M."],
                     "Öğrenci Sayısı":[1500,1200,500,250,300]}

tablo = pd.DataFrame(sozluk)
tablo

fakülte = tablo.groupby("Fakülte")
fakülte.count()
fakülte.mean()
fakülte.min()
fakülte.max()
fakülte.describe()