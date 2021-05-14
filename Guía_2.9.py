#Ejercico 9

"""Dada una lista de números (finalizada en cero) determinar cuántos números positivos y
negativos hay en dicha lista."""

numero = int(input('ingrese un numero '))

if(numero > 0):
    print('el numero es positivo')
else:
    if(numero < 0):
        print('el numero es negativo')
    else:
        print('es neutro')
