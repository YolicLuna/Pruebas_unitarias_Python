"""
En Python, todos los objetos que podemos documentar seles llama objetos documentables.
Y tambien poseen el atributo __doc__.
Puntualmente estos objetos son los siguientes: funciones, clases, metodos y modulos.
"""

"""
Aqui ya tenemos la funcion palindromo_2 documentada, asi que lo que haremos es
documentar el modulo, es decir, el archivo objetos_documentables.py.
Tambien vamos a documentar una clase y un metodo.

El modulo se decribe agregando un comentario entre """ """ al principio del archivo, en la primer linea.
Des pues de declarar la clase se añade el comentario y despues de agregar un metodo
se agrega la documentacion del mismo. 
"""

class User:
    """Permite representar un usuario."""

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo user.

        Args:
            username (str): El username de un usuario.
            password (str): El password de un usuario.
        """        