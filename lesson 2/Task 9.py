import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(-10, 10, 1000)
b = np.power((np.sin(2*a)),2)*np.exp(((a+2)/10)**2)
plt.figure(figsize=(8,3))
plt.grid(lw=0.5, ls='--')
plt.plot(a,b, lw = 4.0, color='red')
plt.plot(a,b, lw = 5.0, color='black', zorder=0)
plt.show()
