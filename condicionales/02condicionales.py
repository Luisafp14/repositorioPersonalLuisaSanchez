# 2 mayor o menor de edad

nombre=input("Digite su nombre ")
edad=int(input("ingrese su edad: "))

if edad <= 0:
    print ("ingrese una edad valida")
elif edad >= 100:
    print ("ingrese una edad valida")
elif edad >= 18:
    print(f"Usted {nombre} es mayor de edad")
elif edad < 18 :
    print(f"Usted {nombre} es menor de edad")
else:
    print("ingrese una edad valida")    
print("Fin del programa") 
