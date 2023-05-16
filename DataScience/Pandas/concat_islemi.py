import numpy as np
import pandas as pd

#concat işleminde sütunların ortak olması gerekir

soz1 = {"A": ["a","b","c","d"],
        "B": ["e","f","g","h"],
        "C": [10,20,30,40]}

tablo1 =  pd.DataFrame(soz1, index = range(4))
tablo1

soz2 = {"A": ["i","j","k","l"],
        "B": ["m","n","o","p"],
        "C": [50,60,70,80]}

tablo2 = pd.DataFrame(soz2, index = [4,5,6,7])
tablo2

soz3 = {"A": ["q","r","s","t"],
        "B": ["u","v","w","x"],
        "C": [90,100,110,120]}

tablo3 = pd.DataFrame(soz3, index = [8,9,10,11])
tablo3

concat = pd.concat([tablo1,tablo2,tablo3])
print(concat)