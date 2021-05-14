#Ejercicio 3

"""Dado un número mostrar la tabla de multiplicar del 1 al 10."""

n=int(input("Ingrese un número: "))

for n in range(1,10):
    print("---Tabla "+str(n)+"---")
    for i in range(10):
        resultado = i*n
        print(i, "x", "=", resultado)
