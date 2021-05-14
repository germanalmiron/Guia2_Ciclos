#Ejercicio 14

"""Se desea procesar los resultados de una encuesta 
respecto a preferencias de los usuarios respecto a redes sociales
(las opciones son Twiter, Instagram, Facebook, otras), determinar la red 
social de mayor preferencia y la menor preferencia, determinar además el
porcenteje que representa la más preferida sobre el total."""

red_social = input("Ingrese red social preferida Twitter, Instagram, Facebook, otras: ")

cont_tw = 0
cont_in = 0
cont_fa = 0
cont_ot = 0

while(red_social != ''):
    if(red_social == 'Twitter'):
        cont_tw += 1
    elif(red_social == 'Instagram'):
        cont_in += 1
    elif(red_social == 'Facebook'):
        cont_fa += 1
    else:
        cont_ot += 1
    red_social = input("Ingrese red social preferida Twitter, Instagram, Facebook, otras ")

red_mayor = 'Tiwtter'
mayor = cont_tw

if(cont_in > mayor):
    mayor = cont_in
    red_mayor = 'Instagram'
if(cont_fa > mayor):
    mayor = cont_fa
    red_mayor = 'Facebook'
if(cont_ot > mayor):
    mayor = cont_ot
    red_mayor = 'otro'

red_menor = 'Tiwtter'
menor = cont_tw

if(cont_in < menor):
    menor = cont_in
    red_menor = 'Instagram'
if(cont_fa < menor):
    menor = cont_fa
    red_menor = 'Facebook'
if(cont_ot < menor):
    menor = cont_ot
    red_menor = 'otro'


print('La red de mayor preferencia es:', red_mayor, mayor)
print('La red de menor preferencia es:', red_menor, menor)















