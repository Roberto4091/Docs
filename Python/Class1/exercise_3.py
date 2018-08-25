# Calcular el volumen de una esfera dado su radio
PI = 3.14
radio = int(input("Ingrese el radio: "))
# Formula para obtener volumen:
# V = (4 * PI * R**3) / 3
volumen = (4 * PI * radio**3) / 3
# Convierto el tipo de dato de las variables a
# string para poder concatenar
print("Volumen: " + str(volumen))
