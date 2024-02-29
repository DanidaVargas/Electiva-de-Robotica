import numpy as np

rad = np.radians(-90)

matriz_rotacion_x = np.array([[1, 0, 0],
                              [0, np.cos(rad), -np.sin(rad)],
                              [0, np.sin(rad), np.cos(rad)]])

matriz_rotacion_y = np.array([[np.cos(rad), 0, np.sin(rad)],
                              [0, 1, 0],
                              [-np.sin(rad), 0, np.cos(rad)]])

matriz_rotacion_z = np.array([[np.cos(rad), -np.sin(rad), 0],
                              [np.sin(rad), np.cos(rad), 0],
                              [0, 0, 1]])

with np.printoptions(precision=0):
    print(f"\nMatriz de rotación en X:\n{matriz_rotacion_x}")
    print(f"\nMatriz de rotación en Y:\n{matriz_rotacion_y}")
    print(f"\nMatriz de rotación en Z:\n{matriz_rotacion_z}")



