import numpy as np

dizi = np.array([[5,15,25], 
                [35,45,55]])

np.sum(dizi) #tüm elemanları topladı
np.prod(dizi) #tüm elemanları yan yana koyup çarptı

np.sum(dizi, axis=1) #satırları kendi aralarında topladı
np.sum(dizi, axis=0) #sütunları kendi aralarında topladı

np.prod(dizi, axis=1) #satırlar kendi aralarında çarptı
np.prod(dizi, axis=0) #sütunları kendi aralarında çarptı

