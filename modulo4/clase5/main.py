import numpy as np

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros)

# usando numpy
np_numeros = list(np.arange(1, 10))
print(np_numeros)
print(1 == np.int64(1))

# matrices
lista_matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(lista_matriz)
print(matriz)
print(type(matriz))

suma = matriz[0] + matriz[1]
print(suma)

# suma de un solo valor
suma_valor = matriz[0, 0] + matriz[1, 2]
print(suma_valor)

# calculos estadísticos
data = np.array([12, 15, 20, 18, 25, 30, 22, 19])

# media
mean = np.mean(data)
print(mean)

# desviacion estandar
std = np.std(data)
print("Desviación estándar : ", std)

# máximos y mínimos
max_val = np.max(data)
max_index = np.argmax(data)
print("Máximo : ", max_val, " Indice : ", max_index)
