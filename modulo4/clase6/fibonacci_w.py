
def fibonacci(valor):
    a = 0
    b = 1
    lista = [0, 1]
    while a + b <= valor:
        suma = a + b
        lista.append(suma)
        a = b
        b = suma
    return lista


if __name__ == "__main__":
    valor = int(input("Ingrese valor fibonacci: "))
    print(fibonacci(valor))
