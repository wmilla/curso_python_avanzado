import decimal

num1 = decimal.Decimal('10.345')
num2 = decimal.Decimal('5.678')

suma = num1 + num2
print("Suma : ", suma)

resta = num1 - num2
print("Resta : ", resta)

division = num1 / num2
print("División : ", division)

redondeo_2 = division.quantize(decimal.Decimal('0.00'))
print(redondeo_2)

redondeo_alza = division.quantize(
    decimal.Decimal('1.00'),
    rounding=decimal.ROUND_CEILING
    )
redondeo_baja = division.quantize(
    decimal.Decimal('1.00'),
    rounding=decimal.ROUND_FLOOR
    )
redondeo_cercano = division.quantize(
    decimal.Decimal('1.00'),
    rounding=decimal.ROUND_HALF_EVEN
    )

print("Redondeo hacia arriba : ", redondeo_alza)
print("Redondeo hacia abajo : ", redondeo_baja)
print("Redondeo cercano : ", redondeo_cercano)
