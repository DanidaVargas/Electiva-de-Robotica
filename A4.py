R0 = 100  

A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12
TEMP = 25
    
R = R0 * (1 + A * TEMP + B * TEMP**2 + C * (TEMP - 100) * TEMP**3)

print(f"\nLa resistencia a {TEMP} grados celsius, debe ser de: {R:.2f} ohmios\n") 
