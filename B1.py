corriente = float(input("\nIngrese el valor de corriente (en amperios): "))
voltaje = float(input("Ingrese el valor de voltaje (en voltios): "))

potencia = voltaje * corriente

print(f"\nLa potencia consumida por el circuito es: {potencia:.2f} vatios")
