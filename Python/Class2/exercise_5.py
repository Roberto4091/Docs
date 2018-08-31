# Ejercicio 2.4.
nro_one = int(input("Ingrese primer nro: "))
nro_two = int(input("Ingrese segundo nro: "))

for i in range(nro_one, nro_two + 1):
    if i % 2 == 0:
        print(i)
