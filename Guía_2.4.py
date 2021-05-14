#Ejercicio 4

"""Dada las notas de los 18 alumnos de un curso determinar cantidad de aprobados y
desaprobados, y además el promedio de nota de los aprobados."""


suma = 0

aprobado = 0

for i in range(0, 3):
    nota = float(input("Ingrese la nota del alumno: "))
    if(nota >= 6):
        suma += nota
        aprobado += 1
        print("Aprobó la materia")
    else:
        print("No aprobó la materia")

print("El promedio es", suma/aprobado)
print("La cantidad de alumnos aprobados es ", aprobado)
