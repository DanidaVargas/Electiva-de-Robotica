import numpy as np

matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz2 = np.array([[7, 8, 9],
                    [4, 5, 6],
                    [1, 2, 3]])

suma_matrices = matriz1 + matriz2
resta_matrices = matriz1 - matriz2
producto_punto = np.dot(matriz1, matriz2)
producto_cruz = np.cross(matriz1, matriz2)

print(f"Suma de matrices: \n{suma_matrices}")
print(f"\nResta de matrices:\n {resta_matrices}")
print(f"\nProducto punto de matrices: \n{producto_punto}")
print(f"\nProducto cruz de matrices: \n{producto_cruz}")

# Si en la matriz hay algun cero, se utiliza funcion 
#(matriz2_no_cero = matriz2 + 1e-9) para delimitar divisiones por cero
division_matrices = np.divide(matriz1, matriz2)
print("\nDivisión de matrices:")
with np.printoptions(precision=2):
    print(division_matrices)
    