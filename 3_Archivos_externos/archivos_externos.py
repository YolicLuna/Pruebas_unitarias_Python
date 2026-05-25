"""
Algo que se tiene que tener presente al utilizar el modulo doctest es que no es un frmaework de testing.
Ya que no tiene ciertas funciones para realizar las pruebas unitarias, principalmente en casos en los que
se requiera implementar cieta logica de programacion, o sea, creando nuevas variables, 
constantes, implementando ciclos, condiciones, importando modulos, etc.

Y si, eso se puede hacer dentro del doctsring, eso no es correcto, ya que recordemos que el docstring esta
diseñado para documentar objetos y no para testearlos. 
Por lo tanto, el agregar logica de programacion en la documentacion, simplemente no esta bien. 
Pero lo que si podemos hacer es crear un archivo independiente en dodne coloquemos exclusivamente todo el codigo
necesario para poder implementar los casos de prueba.
Asi se separa la documentacion del codigo necesario para realizar las pruebas. 
"""

"""
Loq ue haremos es que moveremos los casos de pueba a un archivo independeinte con la finalidad de separar
la documentacion de las pruebas.
Para ellos se crea un archivo de texto, por convencion, todos los archivos dedicados a testear o provar funcionalidades
deben comenzar con el prefijo test_ seguido del nombre.
"""


def palindromo_2 (sentence: str) -> bool:
    """Permite conocer su un string es o no un palindromo.

    Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False.
    """    
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]


"""
En este caso, en la terminal, ejecutaremos 'python -m doctest test_main.txt'
"""


"""
Para probar la clase, primero se debe crear un nuevo objeto y despues las pruebas.
Esto se puede ver en el test_main.txt.
"""

class User:
    """Permite representar un usuario."""

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo user.

        Args:
            username (str): El username de un usuario.
            password (str): El password de un usuario.
        """

        self.username = username
        self.password =password