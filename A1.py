import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

suma = vector_a + vector_b
resta = vector_a - vector_b
producto_punto = np.dot(vector_a, vector_b)
producto_cruz = np.cross(vector_a, vector_b)

print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto punto: {producto_punto}")
print(f"Producto cruz: {producto_cruz}")
