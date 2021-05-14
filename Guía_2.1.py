#Ejercicio 1 

"""Ingresar 10 numeros e indicar los que son multiplos de 2 y de 3."""

for i in range(0, 10):
    numero = int(input("Ingrese un número:  "))
    if(numero % 2 == 0 and numero % 3 == 0):
        print("Es múltiplo de 2 y de 3")

