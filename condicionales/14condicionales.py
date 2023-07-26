# 14 numero de pulsaciones

def calcular_pulsaciones(edad, genero):
    if genero == 1:  # Género femenino
        pulsaciones = (220 - edad) / 10
    elif genero == 2:  # Género masculino
        pulsaciones = (210 - edad) / 10
    else:
        raise ValueError("Error: El valor del género debe ser 1 para femenino o 2 para masculino.")
    return pulsaciones

try:
    edad = int(input("Ingrese su edad: "))
    genero = int(input("Ingrese su género (1 para femenino, 2 para masculino): "))

    if genero not in [1, 2]:
        print("Error: El valor del género debe ser 1 para femenino o 2 para masculino.")
    else:
        pulsaciones = calcular_pulsaciones(edad, genero)
        print(f"El número de pulsaciones por cada 10 segundos de ejercicio es: {pulsaciones:.2f}")
except ValueError:
    print("Error: Ingrese valores numéricos válidos para la edad y el género.")
