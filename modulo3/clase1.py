cadena = "Python es genial"
caracter = cadena[7:11]
print(caracter)
caracter2 = cadena[0:10:2]
#  el 2 es el paso, es decir, que se salta un caracter
print(caracter2)
reversa = cadena[::-1]
#  los :: significa que se va a recorrer toda la cadena,
#  y el -1 significa que se va a recorrer de derecha a izquierda
print(reversa)

lenguajes_programacion = "Python php go c# javascript java"
lista_lenguajes = lenguajes_programacion.split(" ")
# convierte la cadena en una lista, separando por el espacio " "
print(lista_lenguajes)

print(lista_lenguajes[2:4])
print(lista_lenguajes[0:4:2])


email = "usuario@ed.team"
dominio = email[email.index("@") + 1:]
print(dominio)
