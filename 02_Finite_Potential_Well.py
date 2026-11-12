import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

V0 = 20
a = 1
h2_2m = 3.81
z0 = a*np.sqrt(V0/h2_2m)

def even(z):
    return z*np.tan(z) - np.sqrt(z0**2-z**2)

def odd(z):
    return -z/np.tan(z) - np.sqrt(z0**2-z**2)

z = np.linspace(0.01, z0-0.01, 500)
plt.plot(z, [even(x) for x in z], label="Even")
plt.plot(z, [odd(x) for x in z], label="Odd")
plt.axhline(0)
plt.xlabel("z")
plt.ylabel("Equation")
plt.title("Finite Potential Well")
plt.legend()
plt.grid()
plt.show()
