# Docstring
"""
Con el Docstring podrémos documentar nuestro codigo, ya sean funciones, clases, metodos, modulos, paquetes, etc.
Para un ejemplo, definamos una función que nos permita saber si 
un string es un palindromo.
"""

"""
Vamos a definir una función llamada 'palimdormo', resivira el paramatero 'sentences' que sera del tipo 'str' (string),
y la funcion retornara un objeto de tipo boleano, verdadero o falso, dependiendo de si el parametro es o no un palindromo.
Dentro de la función estandarizamos el string convirtiendo todos sus caracteres en minusculas usando .lower(),
despues reemplazaremos todos los espacios en blanco por nada usando .replace(' ', '').
Por ultimo usaremos return para retornar si la sentencia se lee igual de izquierda a derecha y de derecha a izquierda.
Y le agregamos un comentario de documentación.
"""

def palindromo (sentence: str) -> bool:
    """Permite conocer su un string es o no un palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.
    """    
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]


"""
Lo interesante es que Python, al percatarce de los objetos contienen docstrings 
almacena todo su contenido en el objeto __doc__.
Recordemos que para Python todo es un objeto y eso incluye a las funciones.
Asi que, para nuestra funcion, encontraremos su documentación en el objeto __doc__.

Otra cosa importante, para Python no existe documentación buena o mala,
nosotros decidimos que y como documentar. 
"""


"""
Algo interesante del docstring es que nosotros es que nosostros podemos probar nuestro codigo atraves de el.
En Phyton nosotros podemos probar el correcto funcionamiento de nuestro codigo mediante comentarios.
Y para ello vamos a usar el modulo, doctest.
Para ello, dentro del docstring agregaremos la parte de Ejemplos, despues simularesmos que estamos en el sheld interactivo. Recordemos que en el sheld interactivo, las sentencias se encuentran precedidas por >>>, entonces, para poder ejecutar la funcion, vamos a colocar el llamado de la funcion precedido de >>>, seguido del resultado esperado. 
"""

def palindromo_2 (sentence: str) -> bool:
    """Permite conocer su un string es o no un palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.
    
    Ejemplos:

    >>> palindromo_2('Anita lava la tina')
    True

    >>> palindromo_2('Codigo Facilito')
    False

    >>> sentence = 'Oso'
    >>> palindromo_2(sentence)
    True
    """    
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

"""
Para probar lo anterior, vejecutamos en la terminal 'python -m doctest docstring.py'.
La -m nos permite ejecutar un modulo de Python, en este caso, doctest, modulo que ya se encuentra en la biblioteca estandar de Python.
Ese comando lo que hara es que se ejecuten todas las sentencias que se encuentren en todos los docstrings de todos lo objetos del archivo.

Si al ejecutar en consolo no muestra nada, eso es señal de que todo esta bien, a menos claro de que muestre algun error.
Si queremos obtener mas informacion sobre el resultado, solo debemos sumar -v al final del comando.
"""
