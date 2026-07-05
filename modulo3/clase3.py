texto = """
Python es uno de los lenguajes de programación dinámicos más populares
que existen entre los que se encuentran Java, JavaScript, Go y C#.
Aunque es considerado a menudo como un lenguaje "scripting",
es realmente un lenguaje de propósito general. En la actualidad,
Python es usado para todo, desde simples "scripts",
hasta grandes servidores web que proveen servicio ininterrumpido 24x7.
Es utilizado para la programación de interfaces gráficas y bases de datos,
programación web tanto en el cliente como en el servidor (Django o Flask) y
testing de aplicaciones. Además tiene una amplia aceptación por científicos
que hacen aplicaciones para las supercomputadoras más rápidas del  mundo
y por los niños que recién está comenzando a programar."""

texto = texto.replace("Python", "python")
busqueda_palabra = input("Ingrese la palabra a buscar: ")
index = texto.find(busqueda_palabra)

if index != -1:
    print(f"primer :{busqueda_palabra} se encuentra en el índice {index}")
    total_encontrados = texto.count(busqueda_palabra)
    print(
        f"{busqueda_palabra} se encontró {total_encontrados}"
        f"veces en el texto")
else:
    print(f"{busqueda_palabra} no se encontró en el texto")
