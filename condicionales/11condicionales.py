# 11 Precio a pagar 

def calcular_precio_pizza(tamano, ingredientes_adicionales):
    precios = {1: 15000, 2: 24000, 3: 36000}
    precio_tamano = precios.get(tamano, 0)
    if precio_tamano == 0:
        return "Error: Tamaño de pizza no válido"
    
    costo_ingredientes = ingredientes_adicionales * 4000
    precio_total = precio_tamano + costo_ingredientes
    return precio_total

try:
    tamano_pizza = int(input("Ingrese el tamaño de la pizza (1, 2 o 3): "))
    ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))
    if tamano_pizza not in [1, 2, 3] or ingredientes_adicionales < 0:
        print("Error: Ingrese un tamaño válido de pizza y un número válido de ingredientes adicionales.")
    else:
        precio_final = calcular_precio_pizza(tamano_pizza, ingredientes_adicionales)
        if type(precio_final) == str:
            print(precio_final)
        else:
            print(f"El precio total a pagar es: ${precio_final:,}")
except ValueError:
    print("Error: Ingrese valores numéricos válidos para el tamaño de la pizza y el número de ingredientes adicionales.")
