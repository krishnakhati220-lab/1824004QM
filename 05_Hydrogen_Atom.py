import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 10, 200)

u1 = r*np.exp(-r)
u2 = r*(1-r/2)*np.exp(-r/2)

plt.plot(r, u1, label="Ground state")
plt.plot(r, u2, label="First excited state")
plt.xlabel("r")
plt.ylabel("u(r)")
plt.title("Hydrogen Atom")
plt.legend()
plt.grid()
plt.show()

print("Ground state energy = -13.6 eV")
print("First excited energy = -3.4 eV")
