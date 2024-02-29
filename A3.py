import math as m

x, y, z = 7, 8, 22

def rect_c(x, y, z):
    r = (x**2 + y**2)**0.5  
    theta = m.atan2(y, x)  
    return r, theta, z

def rect_e(x, y, z):
    r = (x**2 + y**2 + z**2)**0.5  
    theta = m.atan2(y, x)  
    phi = m.atan2((x**2 + y**2)**0.5, z)  
    return r, theta, phi

r_c, theta_c, z_c = rect_c(x, y, z)
print("\nCoordenadas cilíndricas:")
print(f"r = { r_c:.2f}")
print(f"theta = {theta_c:.2f}")
print(f"z = {z_c:.2f}")

r_e, theta_e, phi_e = rect_e(x, y, z)
print("\nCoordenadas esféricas:")
print(f"r = {r_e:.2f}")
print(f"theta = {theta_e:.2f}")
print(f"phi = {phi_e:.2f}\n")
