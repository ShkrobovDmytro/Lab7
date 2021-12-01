#variant 5
from matplotlib import pyplot as plt
import numpy as np
#Y(x)=15*sin(10*x)*cos(3*x), x=[-3...3]

x = np.arange(-3,3)
y = 15 * np.sin(10*x) * np.cos(3*x)

fig, ax = plt.subplots()
plt.plot(x,y)
plt.show()

fig.savefig("мой график")
print("Ваш график сохранён возле файла .py")