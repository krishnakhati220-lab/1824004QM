import numpy as np
import matplotlib.pyplot as plt

L = 1
h = 1
x = np.linspace(0, L, 200)

for n in range(1, 4):
    psi = np.sqrt(2/L)*np.sin(n*np.pi*x/L)
    plt.plot(x, psi, label="n = "+str(n))

plt.xlabel("x")
plt.ylabel("Wavefunction")
plt.title("Particle in a Box")
plt.legend()
plt.grid()
plt.show()

for n in range(1, 4):
    E = n**2*np.pi**2/2
    print("n =", n, " Energy =", E)
