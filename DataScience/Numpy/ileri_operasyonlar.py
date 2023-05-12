import numpy as np

dizi = np.arange(5)
dizi.shape

dizi2 = np.array([[0,1,2,3,4,5]])
dizi2.shape

dizi2.shape = 3,2
dizi2

dizi2.reshape(2,3)
dizi2

matris = np.array([[1,2,3], #transpozesini alacağız(satırları sütuna çevireceğiz)
                  [4,5,6,],
                  [7,8,9]]) 

matris.T

matris2 = np.array([[10,20,30], 
                    [40,50,60],
                    [70,80,90]])

matris3 = np.concatenate((matris,matris2)) #2 matrisi concatenate ile birleştireceğiz
matris3

matris4 = np.concatenate((matris,matris2), axis=1)
matris4

matris5 = np.vstack((matris,matris2)) #vertical(dikey), axis=0 ile aynı işlemi yapar
matris5

matris6 = np.vstack((matris,matris2)) #horizontal(yatay), axis=1 ile aynı şeyi avr
matris6