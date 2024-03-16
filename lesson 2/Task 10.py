import matplotlib.pyplot as plt
import numpy as np
a = 4
b = 1
c = 20
x = np.linspace(-3*np.pi, 3*np.pi, 250)
s = np.random.normal(1, 4, 250)/20
y = np.sin(x) + s
#y = np.sin(x)+(((1/(a*np.sqrt(2*np.pi)))*np.exp((-(x-b)**2)/2*(a**2)))/c)
plt.figure(figsize=(10, 5))
plt.scatter(x, y)
plt.scatter(x, y,
 s=300,
 marker='s',
 c='violet',
 lw=2,
 edgecolor='black',
 hatch='**'
 )
plt.title(
 label='$sin(x)$ with random noise',
 fontsize=20
)
plt.xlabel('x range', fontsize=18)
plt.ylabel('y range', fontsize=18)
plt.tick_params(labelsize=16)
plt.xticks(
 ticks=np.arange(-10, 11, 2)
)
plt.yticks(
 ticks=np.arange(-1.5, 2,0.5),
 labels=['7', '6', '5', '4', '3', '2', '1 ='][::-1])
plt.show()
