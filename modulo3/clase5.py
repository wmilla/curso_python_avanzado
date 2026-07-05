import re

cadena = "vamos a aprender expresiones regulares con python"
busqueda = re.search("aprender", cadena)
print(busqueda)

# Busqueda en base a un patrón
texto = ("La fecha de vencimiento es 2023-12-31 "
         "y la fecha de inicio es 2023-01-15."
         )
patron_fecha = r"\d{4}-\d{2}-\d{2}"  # \d significa dígito.
fechas_encontradas = re.findall(patron_fecha, texto)
print(fechas_encontradas)

# Reemplazo de texto basado en patrones
texto = " el número de teléfono es 213-374-1234"
patron_numero = r"\d{3}-\d{3}-\d{4}"
nuevo_texto = re.sub(patron_numero, "XXX-XXX-XXXX", texto)
print(nuevo_texto)

# Extracción de urls de un html
html = '<p>Enlace uno <a href="https://www.google.com">Enlace 1</a>'
patron_url = r'<a href="(.*?)">(.*?)</a>'
enlaces = re.findall(patron_url, html)
for enlace in enlaces:
    url, texto = enlace
    print(f"URL: {url}, Texto: {texto}")
