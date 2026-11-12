import numpy as np
import matplotlib.pyplot as plt

D = 0.7555
alpha = 1.44
r0 = 0.1313
r = np.linspace(0.05, 1, 300)
x = r-r0
V = D*(np.exp(-2*alpha*x)-2*np.exp(-alpha*x))

plt.plot(r, V)
plt.xlabel("r")
plt.ylabel("V(r)")
plt.title("Morse Potential")
plt.grid()
plt.show()
