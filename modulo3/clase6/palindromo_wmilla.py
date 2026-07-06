"""
Palindromo
"""

texto = ("""
        Ana y Otto navegaban en un kayak mientras un radar detectaba un rotor
        que giraba sobre ellos. Al llegar al pueblo, leyeron la palabra
        reconocer grabada en una piedra y comprobaron que el agua del lago
        mantenía un nivel muy alto. Antes de regresar, visitaron una tienda
        llamada Salas, cuyo dueño les contó la historia de un ingeniero
        llamado Arenera, famoso por diseñar sistemas de radar.
"""
         )

texto_revez = texto[::-1]
lista_texto = texto.split(" ")
lista_texto_clean = [x.strip() for x in lista_texto if x.strip()]
lista_texto_revez = texto_revez.split(" ")
lista_texto_revez_clean = [x.strip() for x in lista_texto_revez if x.strip()]

palindromo = []

for normal in lista_texto_clean:
    for revez in lista_texto_revez_clean:
        if normal == revez:
            palindromo.append(revez)

palindromo_clean = []

for elemento in palindromo:
    if elemento not in palindromo_clean:
        palindromo_clean.append(elemento)

print(palindromo_clean)
