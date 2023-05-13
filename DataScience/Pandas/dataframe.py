import pandas as pd
import numpy as np


data = np.random.rand(5,4) #randn() olursa negatif değerlerde üretebilir
data

dataframe = pd.DataFrame(data) #dataframe = pd.DataFrame(data)
dataframe


idx = ("A", "B", "C", "D", "E")
col = ("X", "Y", "Z","T")
dataframe2 = pd.DataFrame(data, index = idx, columns = col)
dataframe2

dataframe2["Z"] #Z sütununda çalış
dataframe2[["Z","X"]] #Z ve X sütununda çalış