import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 2, 200)
k = 100

for b in [0, 10, 30]:
    V = 0.5*k*r**2 + (b/3)*r**3
    plt.plot(r, V, label="b = "+str(b))

plt.xlabel("r")
plt.ylabel("V(r)")
plt.title("Anharmonic Oscillator")
plt.legend()
plt.grid()
plt.show()
