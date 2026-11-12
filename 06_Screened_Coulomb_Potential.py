import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.1, 10, 200)

a1 = 3
a2 = 5
a3 = 7

V1 = -np.exp(-r/a1)/r
V2 = -np.exp(-r/a2)/r
V3 = -np.exp(-r/a3)/r

plt.plot(r, V1, label="a = 3")
plt.plot(r, V2, label="a = 5")
plt.plot(r, V3, label="a = 7")
plt.xlabel("r")
plt.ylabel("V(r)")
plt.title("Screened Coulomb Potential")
plt.legend()
plt.grid()
plt.show()
