# 8 orden de los numeros 

Primernumero=int(input("Digite el primer numero "))
segundonumero=int(input("Digite el segundo numero "))
tercernumero=int(input("Digite el tercer numero "))

if Primernumero <= segundonumero <= tercernumero:
    print(f"{Primernumero}, {segundonumero}, {tercernumero}")
elif Primernumero >= segundonumero <= tercernumero:
    print(f"{Primernumero}, {tercernumero}, {segundonumero}")
elif Primernumero <= segundonumero >= tercernumero:
    print(f"{segundonumero}, {tercernumero}, {Primernumero}")
else:
    print(f" Fin del programa")
  