import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(1,10,10)
dizi2 = dizi1**2

fig1 = plt.figure()
fig2 = fig1.add_axes([0.2,0.2,1,1])
fig2.plot(dizi1,dizi2,"g")

#fig1.add_axes 
"""([başka grafiğe göre yatay konum,
   başka grafiğe göre yatay konum,
   genişlik,
   yükseklik])"""

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.7,0.7]) #eksen oluşturduk
ax2 = fig.add_axes([0.1,0.1,0.3,0.3]) #eksen oluşturduk

ax1.plot(dizi1,dizi2, "b.-")
ax1.set_title("Mavi Başlık")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")

ax2.plot(dizi1,dizi2, "r--")
ax2.set_title("Kırmızı Başlık")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
plt.show()

fig.savefig("Figure.png", dpi = 200) #dpi: çözünürlük