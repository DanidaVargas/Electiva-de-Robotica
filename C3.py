
import numpy as np
import matplotlib.pyplot as plt

voltaje = float(input("Ingrese el valor de voltaje (V): "))
capacitancia = float(input("Ingrese el valor de capacitancia (μF): "))
resistencia = float(input("Ingrese el valor de resistencia (Ω): "))

tau = resistencia * capacitancia

tiempo_carga = 5 * tau
tiempo_descarga = 5 * tau

tiempo_c = np.linspace(0, tiempo_carga, 1000)
tiempo_d = np.linspace(tiempo_carga, tiempo_carga + tiempo_descarga, 1000)

voltaje_carga = voltaje * (1 - np.exp(-tiempo_c / tau))
voltaje_descarga = voltaje * np.exp(-(tiempo_d - tiempo_carga) / tau)

#plt.figure(figsize=(10, 6))
plt.plot(tiempo_c, voltaje_carga, label='Carga', color='blue')
plt.plot(tiempo_d, voltaje_descarga, label='Descarga', color='red')
plt.title('Carga y descarga en un circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)
plt.show() 
