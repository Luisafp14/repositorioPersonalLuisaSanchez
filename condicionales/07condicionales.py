# fahrenheit_celsius(): convierte temperatura en grados fahrenheit a grados celsius'''

fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
celsius = (fahrenheit -32 ) * 5.0/9.0
  
#celsius_fahrenheit():convierte temperatura en grados celsius a fahrenheit'''
celsius = int(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = 9.0/5.0 * celsius +32

opcion = int(input('Seleccione una opción: 1.- Fahrenheit a Celsius  2.- Celsius a Fahrenheit '))

if opcion == 1:
     print(fahrenheit())
elif opcion == 2:
        print(celsius())
elif opcion == 3:
        print('Hasta luego')
else:
        print('Ingrese solo números.(1/2)') 