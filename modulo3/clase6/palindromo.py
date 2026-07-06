"""
Palindromo es una palabra o frase que se lee igual
de derecha a izquierda.
"""


def palindromo(str_input):

    str_original = str_input.replace(" ", "").lower()
    str_reverso = str_input[::-1].replace(" ", "").lower()

    if (str_original == str_reverso):
        print("Es un palindromo")
    else:
        print("No es un palindromo")


if __name__ == "__main__":
    str_input = input("Ingrese una frase: ")
    palindromo(str_input)
