P = 5 
d_piston = 0.1  
l_cilindro = 0.5 

A_piston = (d_piston / 2)**2 * 3.1416
F_avance = P * A_piston 
A_superficie = (d_piston / 2) * 3.1416 * 2 * l_cilindro
F_retroceso = P * A_superficie - P * A_piston 

print(f"\nFuerza de avance del cilindro: {F_avance:.3f} N")
print(f"Fuerza de retroceso del cilindro: {F_retroceso:.3f} N\n")
