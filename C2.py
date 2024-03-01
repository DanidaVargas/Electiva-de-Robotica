
import numpy as np
import matplotlib.pyplot as plt

print("Ingrese los coeficientes de la función de transferencia de segundo orden:")
a = float(input("Coeficiente a (de s^2): "))
b = float(input("Coeficiente b (de s): "))
c = float(input("Coeficiente c (término independiente): "))

omega_n = np.sqrt(a)
zeta = b / (2 * np.sqrt(a))

if zeta < 1:
    tipo_sistema = "Subamortiguado"
elif zeta == 1:
    tipo_sistema = "Críticamente amortiguado"
else:
    tipo_sistema = "Sobreamortiguado"

print(f"Tipo de sistema:{tipo_sistema}")

def funcion_transferencia(t):
    return c * (1 - np.exp(-zeta * omega_n * t) * (np.cos(np.sqrt(1 - zeta**2) * omega_n * t) + (zeta / np.sqrt(1 - zeta**2)) * np.sin(np.sqrt(1 - zeta**2) * omega_n * t)))

t = np.linspace(0, 10, 1000)

respuesta = funcion_transferencia(t)

plt.figure(figsize=(10, 6))
plt.plot(t, respuesta, color='blue')
plt.title('Respuesta del sistema en el dominio del tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.grid(True)
plt.show() 
