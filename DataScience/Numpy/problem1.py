#2X3 lük bir A matrisi oluşturun
#3X2 lük bir B matrisi oluşturun

#A ve B matrislerin çarpımını bir C matrisine eşitleyin

import numpy as np

matrisA = np.array([[1,2,3],
                    [4,5,6]])

matrisB = np.array([[7,8],
                   [9,10],
                   [10,11]])

matrisC = np.dot(matrisA,matrisB)
print(matrisC)