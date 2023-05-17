import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veri = np.random.rand(12,1)*10 #12 satır ve bir sütundan oluşan veri topluluğu oluşturduk
veri = veri.round() #float verileri int yaptık
veri

plt.plot(veri,"red")
plt.title("Başlık")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
plt.show()