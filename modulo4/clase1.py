import math
from fractions import Fraction
from decimal import Decimal, getcontext

# Constantes matemáticas
print("pi: ", math.pi)
print("Euler: ", math.e)

# Funciones trigonométricas
angulo = math.radians(45)
print(angulo)
print("Seno: ", math.sin(angulo))
print("Coseno: ", math.cos(angulo))
print("Tangente: ", math.tan(angulo))

# Funciones Exponenciales
print("Exponencial e^2: ", math.exp(2))

# Funciones logarítmicas
print("log neperiano de 10: ", math.log(10))

# Potencias
print("2 elevado al cubo: ", math.pow(2, 3))

# Raices
print("Raíz cuadradad de 25: ", math.sqrt(25))

# Fracciones
frac1 = Fraction(3, 4)
frac2 = Fraction(1, 6)

suma = frac1 + frac2
resta = frac1 - frac2
multiplicacion = frac1 * frac2
division = frac1 / frac2

print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicación: ", multiplicacion)
print("División: ", division)

# Con Libreria decimal
getcontext().prec = 10
num1 = Decimal("0.04554839")
num2 = Decimal("0.44394949")
suma_decimal = num1 + num2

print("Suma decimal: ", suma_decimal)
