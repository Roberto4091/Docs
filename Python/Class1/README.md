# ¿Qué es Python?

Algunas respuestas que salieron al aire:

- Es un lenguaje de programación
- Es orientado a objetos
- Es multiplataforma (puede funcionar en diferentes sistemas operativos y plataformas)
- Es multipropósito (se puede utilizar con distintas finalidades, sea web, desktop o bien para escribir scripts para Arduino, por ejemplo)
- Es multiparadigma (es viable programar no sólo con objetos, sino que además se pueden utilizar programación funcional y estructurada).

Más allá de esto hablamos de cómo Python es, en realidad, **una especificación**. Acá, la especificación completa de [Python 3.7](https://docs.python.org/3.7/reference/index.html).

Luego, a partir de esta especificación, se desarrollaron varias **implementaciones** distintas. Por ejemplo: _CPython_, _IronPython_ y _Jython_, entre otras.

Dos recursos sobre las diferentes implementaciones de Python:

- https://wiki.python.org/moin/PythonImplementations
- https://www.toptal.com/python/por-que-hay-tantos-pythons/es

## Herramientas

Vamos a tener que familiarizarnos con:

- **La consola interactiva de Python:** que sirve para hacer pruebas pequeñas y cortas de lo que queremos hacer con el lenguaje.
- **La consola del sistema operativo:** que vamos a utilizar para ejecutar nuestros programas Python.

Más allá de esto vamos a utilizar _Sublime Text_, aunque si gustan pueden utilizar algún otro editor de texto.

## Entrada y salida

### Mostrar datos en pantalla

¿Queremos mostrar un dato por pantalla? No se diga más, es tan simple como utilizar:

```python
print("Hola mundo")
# Output: Hola mundo
```

Ahora, ¿y si quiero guardar mi nombre en una variable?

```python
nombre = "Python"
print("Hola " + nombre)
# Output: Hola Python
```

_**IMPORTANTE:** Recordemos que en este caso hay que colocar el espacio luego de Hola, ya que de otro modo ambas palabras aparecerían juntas._

### Tomar datos del usuario

Vimos la función `input`, que nos permite tomar un dato tipeado por el usuario y guardarlo en una variable. La utilizamos así:

```python
nombre = input("Ingrese nombre: ")
# Output: Ingrese nombre: Python
print("Este es el curso de " + nombre)
# Output: Este es el curso de Python
```

De este modo, de sólo mostrar datos por pantalla pasamos a poder capturar datos que envíe el usuario.

Fácil, ¿no?

## Variables y tipos de datos

Tuvimos que encarar el siguiente ejercicio: _pedir dos números al usuario y mostrar por pantalla el producto de ambos_.

Con lo que vimos hasta ahora debería ser posible: usando input y print. Esta fue nuestra primera versión del programa:

```python
# ejercicio_1.py
primer_nro = input("Ingrese el 1er nro: ")
segundo_nro = input("Ingrese el 2do nro: ")

print(primer_nro * segundo_nro)
```

Ahora bien: al correrlo, nos encontramos con el siguiente problema:

```bash
$ python3 ejercicio_1.py
Ingrese el 1er nro: 2
Ingrese el 2do nro: 3
Traceback (most recent call last):
  File "test_input.py", line 4, in <module>
    print(primer_nro * segundo_nro)
TypeError: can't multiply sequence by non-int of type 'str'
```

¿Qué pasó? Básicamente estamos **tratando de multiplicar strings**. Recordemos entonces que Python aún sin ser explícitamente tipado (no se coloca el tipo de dato en las variables al declararlas), sí es fuertemente tipado. Esto implica que esta clase de operaciones no es posible.

Por ende, lo que debería pasar es que hagamos una _conversión_ del tipo de dato:

```python
# ejercicio_1.py
primer_nro = int(input("Ingrese el 1er nro: "))
segundo_nro = int(input("Ingrese el 2do nro: "))

print(primer_nro * segundo_nro)
```

Ahora, al ejecutar:

```bash
$ python3 ejercicio_1.py
Ingrese el 1er nro: 4
Ingrese el 2do nro: 5
20
```

En caso de querer mostrar un mensaje un poco más formateado, una opción sería:

```python
primer_nro = int(input("Ingrese el 1er nro: "))
segundo_nro = int(input("Ingrese el 2do nro: "))

print("El producto de ambos nros es: " + str(primer_nro * segundo_nro))
```

Es decir, convirtiendo el resultado del producto a string **antes** de unirlo con el resto del mensaje.

## Ejercicios

Implementar algoritmos que permitan:

1. Calcular el perímetro y área de un rectángulo dada su base y su altura. [Resuelto](./exercise_1.py)
2. Calcular el perímetro y área de un círculo dado su radio. [Resuelto](./exercise_2.py)
3. Calcular el volumen de una esfera dado su radio. [Resuelto](./exercise_3.py)
4. Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1,x2,y1,y2. [Resuelto](./exercise_4.py)
