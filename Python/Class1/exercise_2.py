# Calcular el perimetro y area de un circulo dado su radio
PI = 3.14
radio = int(input("Ingrese el radio: "))
# Formula para obtener perimetro:
# P = PI.R
perimetro = 2 * PI * radio
# Formula para obtener area:
# A = PI.R**2
# Las potencias se calculan con el operador **
area = PI * (radio ** 2)
# Convierto el tipo de dato de las variables a
# string para poder concatenar
print("Perimetro: " + str(perimetro))
print("Area: " + str(area))
