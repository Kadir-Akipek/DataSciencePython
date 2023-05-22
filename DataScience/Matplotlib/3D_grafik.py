import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection = "3d")

z = np.random.rand(10,3) # z eksenini tanımladık
x = z*np.random.rand(10,3)
y = z*np.random.rand(10,3)

ax.plot_surface(x, y, z)
plt.show()

fig = plt.figure(figsize=(10,10)) #grafiğin boyutunu belirledik
ax = plt.axes(projection = "3d")

z = np.random.rand(10,3)
x = z*np.random.rand(10,3)
y = z*np.random.rand(10,3)

ax.plot_surface(x, y, z,color="r")
plt.title("3 Boyutlu Grafik")
plt.show()