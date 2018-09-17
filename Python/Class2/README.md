# Estructura if

En todo lenguaje de programación requerimos que nuestro programa tenga la capacidad de tomar decisiones, y a partir de allí, ejecutar acciones concretas.

Esto normalmente se lleva a cabo con (en principio) la estructura de decisión `if`

Ahora bien, ¿cómo escribimos un if? De la siguiente forma:

```python
if <condición>:
    acción()
```

De lo anterior, debemos prestarle atención a una serie de cuestiones:

1. El funcionamiento básico es: **SI** se cumple `<condición>` (o sea, si `<condición>` es `True`), **ENTONCES** se ejecutará `acción()`.
2. La `<condición>`: es, básicamente, una **expresión lógica** (también conocida como _expresión booleana_) que debe arrojar uno de dos posibles valores: **verdadero** o **falso** (o `True` y `False`, hablando en idioma Python). En la siguiente sección veremos cómo armar expresiones de este tipo.
3. Los dos puntos (`:`) al final de la primera línea: éstos indican que **estamos abriendo una estructura** que anidará más cosas (léase: _otras instrucciones Python_).
4. La tabulación delante de `acción()`: esa tabulación indica que `acción()` se encuentra **dentro** del `if`. Siendo así, cada instrucción que queramos colocar anidada en cualquier estructura, deberá estar tabulada. **SIEMPRE**.

## OPERADORES DE COMPARACIÓN

Como indicamos, para poder hacer uso del `if`, necesitamos poder escribir expresiones lógicas. Para esto, utilizamos los **operadores de comparación**.

Siendo así, tenemos:

- Operador _"igual a"_: `==`
- Operador _"diferente a"_: `!=`
- Operador _"mayor a"_: `>`
- Operador _"mayor o igual a"_: `>=`
- Operador _"menor a"_: `<`
- Operador _"menor o igual a"_: `<=`

Ejemplos:

- edad menor a 18: `edad < 18`
- nro mayor a 5: `nro > 5`
- cantidad igual a 10: `cantidad == 10`
- respuesta distinta de "N": `respuesta != "N"`

**Nótese que las comparaciones pueden darse con distintos tipos de datos.**

### UN EJEMPLO DE IF:

```python
if edad > 17:
    print("Mayor de edad")
```

## else

Ahora bien, ¿qué sucede cuando **NO** se cumple la condición? A priori, no se ejecuta nada. **SALVO** que agreguemos un else a la estructura.

### UN EJEMPLO DE ELSE:

```python
if edad > 17:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

**Nótese que el else también tiene los dos puntos (:) y que también hay una tabulación para marcar lo que hay dentro de su alcance (o sea, en su interior).**

## elif

Imaginemos que queremos tirar distintos mensajes para alguien mayor de 18 o mayor de 21. Con el conocimiento actual, deberíamos hacer algo como:

```python
if edad > 20:
    print("Mayor de edad")
else:
    if edad > 17:
        print("Entre 18 y 21")
    else:
        print("Menor de edad")
```

¿Qué problema tiene esto? De funcionamiento, ninguno. El único asunto que tiene, es que _es feo_.

Es así que podemos utilizar la instrucción `elif` para mejorar este código.

Quedaría más o menos así:

```python
if edad > 20:
    print("Mayor de edad")
elif edad > 17:
    print("Entre 18 y 21")
else:
    print("Menor de edad")
```

**Una vez más: nótese la presencia de los dos puntos (:) y de la correspondiente tabulación.**

## Operadores lógicos

Tenemos además otro caso: el de unir expresiones lógicas. Para ello debemos hacer uso de **operadores lógicos**.

"¿Y quejéso?", por ahí se preguntan. Básicamente operadores que me admiten colocar distintas expresiones lógicas, juntas.

Siendo así, tenemos:

- Operador **Y**: en algunos lenguajes es `&&,` en Python es `and`.
- Operador **O**: en algunos lenguajes es `||`, en Python es `or`.
- Operador **NO**: en algunos lenguajes es `!`, en Python es `not`.

¿Cómo los usamos? Básicamente, _entre_ expresiones lógicas.

### EJEMPO DE USO DE OPERADORES LÓGICOS:

```python
if promedio >= 7 and porcentaje_asistencia >= 70:
  print("Materia aprobada")
else:
  print("Materia desaprobada")
```

# Estructura for

Así como existe la posibilidad de ejecutar acciones en base a decisiones, también existe la posibilidad de _repetir acciones_.

Para esto utilizamos la estructura **for**.

Un ejemplo:

```bash
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>>
```

Acá podemos ver algunas cuestiones:

1. La variable `i`, que se declara al lado del `for`, y luego se utiliza dentro del mismo. A esta variable la denominaremos **variable de iteración**.
2. El uso de `range(5)` que según parece, nos hace recorrer los números **del 0 al 4**. Es decir, **muestra 5 números, comenzando en el 0**.

Otron ejemplo:

```bash
>>> for i in range(2, 7):
...     print(i)
...
2
3
4
5
6
>>>
```

En este caso especificamos dos valores en range. Ahora, como se puede ver, el primer valor lo toma como **origen** y el segundo como **destino**. Sin embargo, al segundo número no llega a tocarlo, sino que se queda en el anterior.

Veamos qué sucede en el siguiente ejemplo:

```bash
>>> for i in range(0, 50, 10):
...     print(i)
...
0
10
20
30
40
>>>
```

Aquí, especificando el tercer valor aparentemente especifica **un salto**. Como en el caso anterior, el primer valor es origen, el segundo es destino (aunque sin tocar el valor).

Por último, nos permite algunas cosas interesantes:

```bash
for i in range(5, 0, -1):
...     print(i)
...
5
4
3
2
1
>>>
```

# Funciones

Todo programa está subdividido en partes más pequeñas. El motivo es simple: _"divide y reinarás"_.

Así, aparece la figura de las funciones. Pequeños bloques de código **con una y sólo una responsabilidad**, los cuales pueden recibir valores para poder trabajar.

A las funciones, igual que con las variables, les asignaremos un nombre. El que, igual que con las variables (sí, de nuevo) **debe ser significativo**.

Asimismo, dado que una función es una acción, se recomienda que el nombre esté compuesto por, al menos, un **verbo**.

Un ejemplo:

```bash
>>> def duplicar(n):
...     print(n*2)
...
>>> duplicar(4)
8
```

Expliquemos:

1. Primero, la función la definimos con la palabra clave `def`, luego el nombre de la función y luego entre paréntesis, los parámetros para la misma.
2. Luego, la ejecutamos colocando su **nombre** y especificando entre los **paréntesis** el valor con el que queremos que trabaje.

**¡IMPORTANTE! Si no queremos que reciba ningún parámetro es tan sencillo como no colocar nada entre los paréntesis en la declaración de la función.**

Ahora, esta función de arriba tiene un problema. ¿Qué sucede si queremos utilizar ese valor y poner algo como _"El doble de 4 es 8"_?

```bash
>>> print("El doble de 4 es", duplicar(4))
8
El doble de 4 es None
```

Obviamente la pregunta es:

![](https://i.ytimg.com/vi/tHw7IIchAZI/hqdefault.jpg)

El problema es simple: `duplicar` **no devuelve ningún valor**.

Por ende, quien utilice la función (en este caso, el `print`) tome el resultado y haga lo que necesite, sino que lo imprime por pantalla.

De ahí que primero se muestre el 8 (por el `print` que hay dentro de `duplicar`) y que luego se muestre el texto con un `None` al final.

Para que funcione correctamente, debemos modificar la función:

```bash
>>> def duplicar(n):
...     return n*2
...
>>> print("El doble de 4 es", duplicar(4))
El doble de 4 es 8
```

Ahora sí, funciona correctamente.

Siendo así la regla general (**y no negociable**) será: **NUNCA** imprimimos en una función, sino que siempre utilizamos `return` y devolvemos el valor que resultado.
