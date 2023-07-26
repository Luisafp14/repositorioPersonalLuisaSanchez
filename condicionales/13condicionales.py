# 13 reporte de salud

def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

def obtener_estado_salud(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

try:
    peso = float(input("Ingrese el peso en Kg: "))
    estatura = float(input("Ingrese la estatura en metros: "))

    if peso <= 0 or estatura <= 0:
        print("Error: Ingrese valores positivos para el peso y la estatura.")
    else:
        imc = calcular_imc(peso, estatura)
        estado_salud = obtener_estado_salud(imc)
        print(f"Su IMC es: {imc:.2f}")
        print(f"Estado de salud: {estado_salud}")
except ValueError:
    print("Error: Ingrese valores numéricos válidos para el peso y la estatura.")
