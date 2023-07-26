# 09 decision de pago 

def tomar_decision_pago(cuenta):
    if cuenta < 150000:
        return "Pago en efectivo"
    elif cuenta <= 300000:
        return "Pago con el celular (dinero electrónico)"
    elif cuenta <= 600000:
        return "Pago con tarjeta de débito"
    else:
        return "Pago con tarjeta de crédito"

try:
    cuenta = float(input("Ingrese el monto de la cuenta: "))
    tipo_pago = tomar_decision_pago(cuenta)
    print(f"Para la cuenta de ${cuenta:.2f}, el tipo de pago sugerido es: {tipo_pago}")
except ValueError:
    print("Error: Ingrese un monto válido.")
