# Pedir por consola base y altura, obtener su area y perimetro
base = int(input("Base: "))
altura = int(input("Altura: "))
# Con la funcion str() convierto el resultado de las operaciones a string
# para poder concatenarlo con un mensaje de igual dato
print("\n\nArea: " + str(base * altura))
print("Perimetro: " + str((2 * base) + (2 * altura)))
