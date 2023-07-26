# 5 Mostrar si un estudiante aprovo o no la materia
 
nombre=input("Digita el nombre del estudiante ")
nota1=float(input("Digite la nota "))
nota2=float(input("Digite la nota "))
nota3=float(input("Digite la nota "))
nota4=float(input("Digite la nota "))
nota5=float(input("Digite la nota "))

promedio=nota1 + nota2 + nota3 + nota4 + nota5 / 5

if promedio >= 3.0:
    print(f"El estudiante {nombre} aprobo la materia")
else:
    print(f"El estudiante {nombre} no aprobo la materia")

print("Fin del programa") 
