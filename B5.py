
while True:

    respuesta = input("¿Desea continuar? (Si/No): ").lower()

    if respuesta == "si":
        continue 
    elif respuesta == "no":
        print("Fin del programa.")
        break 
    else:
        print("Respuesta inválida. Responda con 'Si' o 'No'.")