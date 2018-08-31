# Ejercicio 1.4. B

# Con Recursividad
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# Sin Recursividad


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


nro = int(input("Factorial de: "))
print(factorial(nro))
