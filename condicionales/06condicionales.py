# 6 programa de menu para hallar el area de las figuras geometricas

print("menu")
print("Digite la opcion que quiera aplicar")
elegir=int(print(f"1. Area de un rectangulo   2. Area de un cuadrado   3. Area de un paralelogramo  4. Area de un rombo  5. Area de un trapecio  6. Area de un triangulo  7. Area de un triangulo equilatero  8. Area de un triangulo rectangulo  9. Area de un poligono regular "))
 

if elegir == 1:
    largo=int(print ("Ingrese el largo de su rectangulo "))
    ancho=int(print ("Ingrese el ancho de su rectangulo "))
    areare=largo * ancho
    print(f"El area de su rectangulo es {areare}")
elif elegir == 2:
    largo=int(print ("Ingrese el largo de su cuadrado "))
    areacua=largo ** 2
    print(f"El area de su cuadrado es {areacua}")
elif elegir == 3:
    altura=int(print ("Ingrese la Altura de su paralelogramo "))
    base=int(print ("Ingrese la base de su paralelogramo "))
    areapar=base * altura
    print(f"El area de su paralelogramo es {areapar}")
elif elegir == 4:
    diagonalmenor=int(print ("Ingrese el diagonal menor de su rombo "))
    diagonalmayor=int(print ("Ingrese el diagonal mayor de su rombo "))
    arearom=diagonalmayor * diagonalmenor / 2
    print(f"El area de su rombo es {arearom}")
elif elegir == 5:
    basemenor=int(print ("Ingrese la base menor de su trapecio "))
    basemayor=int(print ("Ingrese la base mayor de su trapecio "))
    altura=int(print ("Ingrese la Altura de su trapecio "))
    areatra=basemayor + basemenor * altura / 2
    print(f"El area de su trapecio es {areatra}")
elif elegir == 6:
    altura=int(print ("Ingrese la Altura de su triangulo "))
    base=int(print ("Ingrese la base de su triangulo "))
    areatri=altura * base / 2
    print(f"El area de su triangulo es {areatri}")
elif elegir == 7:
    altura=int(print ("Ingrese la Altura de su triangulo equilatero "))
    base=int(print ("Ingrese la base de su triangulo equilatero "))
    areatri2=altura * base / 2
    print(f"El area de su triangulo equilatero es {areatri2}")
elif elegir == 8:
    altura=int(print ("Ingrese la Altura de su triangulo rectangulo "))
    base=int(print ("Ingrese la base de su triangulo rectangulo "))
    areatri3=altura * base / 2
    print(f"El area de su triangulo rectangulo es {areatri3}")
elif elegir == 9:
    longitud=int(print ("Ingrese la longitud de su poligono regular "))
    perimetro=int(print ("Ingrese el perimetro de su poligono regular "))
    areapol=longitud * perimetro / 2
    print(f"El area de su poligono regular es {areapol}")
else:
    print("Eliga una opcion correcta")

print("Fin del programa") 