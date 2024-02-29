import math

print("Seleccione el sólido para calcular su volumen:")
print("1. Prisma")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")
opcion = int(input("Ingrese el número correspondiente al sólido: "))

if opcion == 1: 
    base = float(input("Ingrese la medida de la base del prisma: "))
    h = float(input("Ingrese la altura del prisma: "))
    volumen = base * h
    print("El volumen del prisma es:", volumen)
elif opcion == 2:
    base = float(input("Ingrese la medida de la base de la pirámide: "))
    h = float(input("Ingrese la altura de la pirámide: "))
    volumen = (1/3) * base * h
    print("El volumen de la pirámide es:", volumen)
elif opcion == 3:
    h = float(input("Ingrese la altura del cono truncado: "))
    radio1 = float(input("Ingrese el radio menor del cono truncado: "))
    radio2 = float(input("Ingrese el radio mayor del cono truncado: "))
    volumen = (math.pi * h / 3) * (radio1 ** 2 + radio1 * radio2 + radio2 ** 2)
    print("El volumen del cono truncado es:", volumen)
elif opcion == 4:
    h = float(input("Ingrese la altura del cilindro: "))
    radio = float(input("Ingrese el radio del cilindro: "))
    volumen = math.pi * radio ** 2 * h
    print("El volumen del cilindro es:", volumen)
else:
    print("Opción no válida.")