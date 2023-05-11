#transpoze = satır ve sütunların yer değiştirmesidir
#numpy.org

import numpy as np
matris = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matris

matris.ndim #2, dizinin kaç boyutlu olduğunu verir
matris.shape #(3,3), dizinin satır ve sütun uzunluğunu verir
matris.size #9, dizimizde kaç tane eleman olduğun bize verir

matris[0,0] #eleman çağırma, önce satır sonra sütun yazılır
matris[:,] #virgülden öncesi satırı ilgilendirir, sonrası sütunu ilgilendirir
matris[1:]
matris[:,1:]
matris[:,1:2]
matris[2,1] = 35


