import matplotlib.pyplot as plt
 
plt.figure(figsize = (8,8)) #8'e 8'lik bir grafik oluşturduk

x = [15,35,35,15]
y = ["A","B","C","D"]
plt.pie(x, labels = y);
plt.show()

x = [15,35,35,15]
y = ["A","B","C","D"]
e = [0.2,0,0,0]
plt.pie(x, explode = e, labels = y);
plt.show()
