import numpy as np
import matplotlib.pyplot as plt

def create_tridiagonal_matrix(n):
    main_diag = np.full(n, -2.0)
    adjacent_diag = np.full(n - 1, 1.0)

    matrix = (np.diag(main_diag)
              + np.diag(adjacent_diag, k=1)
              + np.diag(adjacent_diag, k=-1))

    return matrix


n = 5
matrix = create_tridiagonal_matrix(n)
print(matrix)

M = create_tridiagonal_matrix(1000)
eigenvalues, eigenvectors = np.linalg.eigh(M)

print(np.round(eigenvalues, 5))
print(np.round(eigenvectors, 5))

plt.figure(figsize=(8, 5))
plt.plot(eigenvalues, marker='o', markersize=2, linestyle='-')
plt.xlabel("Index")
plt.ylabel("Eigenvalue")
plt.title("Eigenvalues of a Tridiagonal Matrix")
plt.show()
