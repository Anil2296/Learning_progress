import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.2*np.pi,0.1)
x = 16*np.sin(t)**3
y=13*np.cos(t)-np.cos(4*t)
plt.plot(x)
plt.show()           
