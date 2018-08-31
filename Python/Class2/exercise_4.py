# Ejercicio 2.3
def fahrenheitToCelsius(fah):
    celsius = (fah - 32) / 1.8000
    return round(celsius, 4)


for i in range(0, 130, 10):
    print(str(i) + "F" + " = " + str(fahrenheitToCelsius(i)) + "C")
