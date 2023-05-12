#iki basamaklı rastgele tam sayılardan oluşan 3X3 lük bir matris oluşturun
#Oluşturduğunuz matrisin transpozesini alın

import numpy as np

a = (np.random.rand(3,3)*100).round()
print(a)
print(a.T)

