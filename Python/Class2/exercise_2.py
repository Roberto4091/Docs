# Ejercicio 2.1.
pesos = int(input("Cantidad de pesos? "))
tasa_interes = int(input("Tasa de interes? "))
cant_anios = int(input("Cantidad de anios? "))

monto_fina = tasa_interes / 100
monto_fina = (1 + monto_fina)**cant_anios
monto_fina = pesos * monto_fina

print("Monto a obtener: " + str(monto_fina))
