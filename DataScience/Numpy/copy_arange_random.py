import numpy as np
"""matris1 = np.array([[1],
                    [4], 
                    [7]])
matris1.shape"""

matris = np.array([[1,2,3], 
                    [4,5,6], 
                    [7,8,9]])
matris.shape

matris2 = matris
matris[1,1] = 150 #matris le ilgili düzenleme yaptığımızda matris 2 de değişti.Bunu istemiyorsak copy yi kullanacağız
matris2

m1 = np.array([ [1,2,3], 
                [4,5,6], 
                [7,8,9]])

m2 = m1.copy()
m1[1,1] = 150
m1
m2

m3 = np.arange(0, 10, 2) #0 dan 10 kadar 2 şer 2 şer ilerle(10 dahil değil)
m3

m4 = np.random.rand(3,3)
m4

