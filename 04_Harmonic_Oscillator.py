import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)

for n in range(3):
    if n == 0:
        psi = np.exp(-x**2/2)
    elif n == 1:
        psi = x*np.exp(-x**2/2)
    else:
        psi = (2*x**2-1)*np.exp(-x**2/2)
    plt.plot(x, psi, label="n = "+str(n))

plt.xlabel("x")
plt.ylabel("Wavefunction")
plt.title("Harmonic Oscillator")
plt.legend()
plt.grid()
plt.show()

for n in range(3):
    E = n + 0.5
    print("n =", n, " Energy =", E)
