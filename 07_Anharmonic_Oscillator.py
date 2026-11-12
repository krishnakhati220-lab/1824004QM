import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal


hbar = 197.3       
m = 940            
k = 100            

b_values = [0, 10, 30]


r = np.linspace(0.001, 3, 1200)
dr = r[1] - r[0]

r_in = r[1:-1]

print("Anharmonic Oscillator")
print()

for b in b_values:

    
    V = 0.5*k*r_in**2 + (b/3)*r_in**3

    
    diagonal = hbar**2/(m*dr**2) + V
    off_diagonal = -hbar**2/(2*m*dr**2) * np.ones(len(r_in)-1)

    
    energy, wavefunction = eigh_tridiagonal(
        diagonal,
        off_diagonal,
        select='i',
        select_range=(0, 0)
    )

    print(f"b = {b} MeV fm^-3")
    print(f"Ground state energy = {energy[0]:.3f} MeV")
    print()


plt.figure(figsize=(8,6))

for b in b_values:
    V = 0.5*k*r**2 + (b/3)*r**3
    plt.plot(r, V, label=f"b = {b}")

plt.xlabel("r (fm)")
plt.ylabel("V(r) (MeV)")
plt.title("Anharmonic Oscillator Potential")
plt.legend()
plt.grid()
plt.show()
