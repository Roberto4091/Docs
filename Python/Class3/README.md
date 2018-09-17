De la clase anterior quedaron un montónnnn de ejercicios, así que gran parte de la clase se fue en ver posibles resoluciones.

Aún así, vimos algunas cosas de relevancia.

# Zen de Python

Colocando `import this` en la consola Python, obtenemos lo siguiente:

```bash
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

En espanol:

```bash
>>> import this
El Zen de Python, por Tim Peters

Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Espaciado es mejor que denso.
La legibilidad es importante.
Los casos especiales no son lo suficientemente especiales como para romper las reglas.
Sin embargo la practicidad le gana a la pureza.
Los errores nunca deberían pasar silenciosamente.
A menos que se silencien explícitamente.
Frente a la ambigüedad, evitar la tentación de adivinar.
Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
A pesar de que esa manera no sea obvia a menos que seas Holandés.
Ahora es mejor que nunca.
A pesar de que nunca es muchas veces mejor que *ahora* mismo.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede que sea una buena idea.
Los espacios de nombres son una gran idea, ¡tengamos más de esos!
```

Por si te estás preguntando _"¿y quejésto?"_. Básicamente principios de software, que en algún momento influyeron al diseño de Python como lenguaje, y que (opinión personal y profesional) cada persona que programe, debería tener presentes.

# PEP 8

Así como existen principios, éstos son un tanto amplios y no indican con exactitud la forma correcta de escribir código Python.

Por esto fue que en algún momento surgió el PEP 8, que indica cómo se debe escribir en Python.

Dicho sea de paso: PEP viene de Python Enhancement Proposal.

Un par de recursos al respecto:

- Una guía completa con ejemplos incluídos: http://pep8.org/
- Lo mismo, pero en español: http://recursospython.com/pep8es.pdf

# Parámetros nombrados

Anteriormente vimos funciones con parámetros. Ahora bien: hay casos en los que ayuda a la legibilidad el uso de parámetros nombrados.

Tomando como ejemplo la función que armamos para convertir horas, minutos y segundos a segundos, podríamos dejar algo más o menos así:

```bash
>>> def convertir_hms_a_segs(hs=0, mins=0, segs=0):
...     resultado = segs
...     resultado += mins * 60
...     resultado += hs * 3600
...     return resultado
...
>>> convertir_hms_a_segs(1,1,1)
3661
>>> convertir_hms_a_segs(hs=2)
7200
>>> convertir_hms_a_segs(mins=15)
900
>>> convertir_hms_a_segs(segs=1, mins=1, hs=1)
3661
```

Notemos entonces que:

1. Todos los parámetros tiene un `=0` luego del mismo. **Esto significa que el valor predeterminado del mismo será 0**. Podríamos haber puesto cualquier cosa, pero en este caso servía el 0.
2. Sigo utilizando las variables como antes: **lo que está definido en los parámetros se usa en la función**.
3. Si al usar la función quiero especificar sólo uno de los parámetros,**es tan sencillo como colocar el nombre del mismo**. Así, podemos especificar sólo horas o minutos como en los dos últimos ejemplos.
4. Asimismo, como muestra el último ejemplo: si quiero usar la función con los parámetros en otro orden, puedo hacerlo.
