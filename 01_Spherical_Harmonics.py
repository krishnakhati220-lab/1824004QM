import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm

l = 2
m = 0

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

Y = sph_harm(m, l, phi, theta)
P = abs(Y)**2

plt.contourf(theta, phi, P)
plt.xlabel("Theta")
plt.ylabel("Phi")
plt.title("Probability Density |Y(l,m)|²")
plt.colorbar()
plt.show()
