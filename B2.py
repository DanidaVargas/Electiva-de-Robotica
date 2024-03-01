import random

inicio = int(input("\nIngrese el valor inicial: "))
fin = int(input("Ingrese el valor final: "))
cantidad = int(input("Ingrese la cantidad de números aleatorios: "))

print("\nNúmeros aleatorios generados:")
for x in range(cantidad):
    num = random.randint(inicio, fin)
    print(num)
    