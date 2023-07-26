# 10 leer numero de llantas

def calcular_valor_a_pagar(num_llantas):
    if num_llantas < 6:
        precio_unitario = 240000
    elif num_llantas <= 7:
        precio_unitario = 221000
    else:
        precio_unitario = 180000
    
    valor_total = num_llantas * precio_unitario
    return valor_total

try:
    num_llantas = int(input("Ingrese el número de llantas a comprar: "))
    if num_llantas <= 0:
        print("Error: El número de llantas debe ser un valor positivo mayor que cero.")
    else:
        valor_total = calcular_valor_a_pagar(num_llantas)
        print(f"El valor a pagar por {num_llantas} llantas es: ${valor_total:,}")
except ValueError:
    print("Error: Ingrese un número válido de llantas.")
