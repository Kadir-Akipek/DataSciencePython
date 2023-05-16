import numpy as np
import pandas as pd

#merge işleminde tüm sütunların ortak olmasına gerek yoktur

soz1 = {"A": ["a","b","c","d"],
        "B": ["x","y","z","t"]}

tablo1 = pd.DataFrame(soz1)
tablo1

soz2 = {"A": ["a","b","c","d"],
        "C": ["e","f","g","h"]}

tablo2 = pd.DataFrame(soz2)
tablo2

merge = pd.merge(tablo1,tablo2, on = "A")
print(merge)
