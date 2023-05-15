#eksik veri ile çalışmak

import numpy as np
import pandas as pd

sozluk = {"A":[10, np.nan, np.nan, 40], "B":[15, np.nan, 20, 25],
          "C":[10, 30, 15, 30],"D":[np.nan, 20, 30, 40]}

tablo = pd.DataFrame(sozluk, index = ["X","Y","Z","T"])
tablo

#dropna() ile eksik verileri veri setinden çıkartacağız
tablo.dropna()

#eksik veri olmayan sütunu bize gösterecek
tablo.dropna(axis=1)

#fillno() eksik verileri dolduracağız
tablo.fillna(15)
