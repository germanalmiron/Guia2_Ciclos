#Ejercicio 2

"""Dada una lista de 15 personas de las que se conoce nombre y edad, 
determinar cúantas son mayopres de edad"""

datos = []

for i in range(0,3):
    nombre = input('Ingrese su nombre: ').capitalize()
    anio_nacimiento = int(input('ingrese año de nacimiento '))
    datos.append(nombre)
    edad = 2021 - anio_nacimiento

    if(edad >= 18):
        print(nombre, "Es mayor de edad")
    else:
        print("Es menor de edad")

