import pandas as pd
import numpy as np

data = np.random.rand(3,3)*10
data = data.round()
data

idx = ["A", "B", "C"]
col = ["X","Y","Z"]
tablo = pd.DataFrame(data, index=idx, columns = col)
tablo

tablo.reset_index()

idx2 = ["AA", "BB", "CC"]
tablo["T"] = idx2 #sütun ekledik
tablo

tablo = tablo.set_index("T") #index değiştireceğiz
tablo

#loc: location
#iloc: index location

c = tablo.loc["CC"] #CC satırını inceledik
c

b = tablo.iloc[[1]] #çift köşeli parantez olursa verileri yatay bir şekilde inceleriz
b