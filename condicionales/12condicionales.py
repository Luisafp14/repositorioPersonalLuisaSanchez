# 12 Promocion de local

def calcular_valor_total(cantidad, precio_unitario):
    descuento = 0
    if cantidad > 5 and cantidad < 10:
        descuento = 0.05
    elif cantidad >= 10:
        descuento = 0.08
    
    precio_con_descuento = precio_unitario * (1 - descuento)
    valor_total = cantidad * precio_con_descuento
    return valor_total

try:
    cantidad = int(input("Ingrese la cantidad de artículos a comprar: "))
    precio_unitario = float(input("Ingrese el precio unitario original: "))
    if cantidad <= 0 or precio_unitario <= 0:
        print("Error: Ingrese valores positivos para la cantidad y el precio unitario.")
    else:
        valor_total_a_pagar = calcular_valor_total(cantidad, precio_unitario)
        print(f"El valor total a pagar por {cantidad} artículos es: ${valor_total_a_pagar:.2f}")
except ValueError:
    print("Error: Ingrese valores numéricos válidos para la cantidad y el precio unitario.")
