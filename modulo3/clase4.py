from datetime import datetime
name = "Cesar"
age = 30
print(f"Hola, mi nombre es {name} y tengo {age} años.")
print("Hola, mi nombre es {} y tengo {} años.".format(name, age+5))

sql_insert = (
    "insert into users (name, age) values ('{}', '{}')"
    .format(name, age)
    )
print(sql_insert)

print("Nombre : {0}, Edad : {1}".format(name, age))

# Print con parámetros
producto = "Celular Iphone 12"
precio = 600

print("Producto: {prod}, Precio: {pre:.2f}".format(prod=producto, pre=precio))

# Formatear números
num = 12345.6789
print("{:.2f}".format(num))
print("{:,}".format(num))
print("{:e}".format(num))

# Formatear fechas
now = datetime.now()
print("Fecha y hora : {:%d-%m-%Y  %H:%M:%S}".format(now))

# Alineación y relleno
number = 42
print("Número : {:>10}".format(number))  # Alineado a la derecha
print("Número : {:0<5}".format(number))  # Relleno con ceros a la izquierda
