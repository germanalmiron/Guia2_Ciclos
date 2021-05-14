#Ejercicio 6

"""Dado 15 números indicar cuál es el mayor."""

maximo = int(input('Ingrese un numero: '))

for i in range (0,15):
    numero = int(input('Ingrese un numero: '))
    if(numero > maximo):
        maximo = numero
        print("El maximo es", maximo)
