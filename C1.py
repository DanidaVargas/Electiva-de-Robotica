import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.linspace(-200, 200, 1000)

a = 3.9083e-3
b = -5.775e-7
c = -4.183e-12

resistencias = 100 * (1 + a * temperaturas + b * temperaturas ** 2 + c * (temperaturas - 100) ** 3)

plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, color='purple')
plt.title('Comportamiento de un sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ohmios)')
plt.grid(True)
plt.show()
