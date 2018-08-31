# Ejercicio 2.2
def fahrenheitToCelsius(fah):
    celsius = (fah - 32) / 1.8000
    return round(celsius, 4)


fahrenheit = int(input("Cantidad de grados Fahrenheit? "))
print("Celsius: " + str(fahrenheitToCelsius(fahrenheit)))
