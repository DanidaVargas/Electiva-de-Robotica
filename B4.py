print("Seleccione el tipo de robot:")
print("1. Robot Cilíndrico")
print("2. Robot Cartesiano")
print("3. Robot Esférico")
opcion = int(input("Ingrese el número correspondiente al tipo de robot: "))

if opcion == 1: 
    tipo = "Robot Cilíndrico"
    articulaciones = "Posee 2 articulaciones (rotacional y lineal)"
elif opcion == 2:
    tipo = "Robot Cartesiano"
    articulaciones = "Posee 3 articulaciones (lineales)"
elif opcion == 3: 
    tipo = "Robot Esférico"
    articulaciones = "Posee 3 articulaciones (rotacionales)"
else:
    tipo = "Opcion no valida"
    articulaciones = "..."

print("Tipo de robot:", tipo)
print("Número de articulaciones:", articulaciones)
