# concatenación
cadena1 = "Hola, "
cadena2 = "¿Cómo estás?"
resultado = cadena1 + cadena2
print(resultado)

# concatenación con f-strings
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
saludo = f"Hola mi nombre es {nombre} {apellido} y tengo {edad} años"
print(saludo)

# concatenar con listas
numero = [1, 2, 3, 4, 5]
resultado = ""
for num in numero:
    resultado += str(num) + " "
print(resultado)

# concatenar con join
palabras = ["Hola", "mi", "nombre", "es", "Python"]
frase = " ".join(palabras)
print(frase)
