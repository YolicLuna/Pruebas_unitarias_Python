import logging



"""
Otra forma de probar nuestro codigo es mediante impresiones. 
Es decir, agregamos prints en ciertas partes de nuestro codigo para saber
como se va ejecutando el programa, en el momento en que falle, los print se detendran
y asi podremos saber por donde comenzar a revisar nuestro codigo.

Pero lo mejor que podemos hacer para realizar este tipo de pruebas es hacer uso del
modulo logging de Python.
Este modulo permite trabajar con 5 tipos de mensaje y se encuentran ordenados por nivel de prioridad: 
debug = 10 
info = 20 
warning = 30 
error = 40
critical = 50

Al ejecutar nuestro programa, solo se mostraran los niveles que sean igual o mayor a 30.
Es por eso que usamos logging.basicConfig con un nivel de debug, indicando que queremos que
se muestren los niveles apartir de que sean iguales o mayores a 10.
Tambien podeos modificar quien o que ejecuto el programa, añadiendo format='%()s',
dentro de los parentesis podemos añadir proces (numero de proceso), procesName (nombre del proceso), 
thread (numero del thread del proceso.) o threadeName (nombre del threade).
Usamos %(levelname)s para conocer el nivel, que seria uno de los 5 mencionados anteriormente. 
Y usamos %(asctime)s para conocer el momento exacto en que se corrio el programa.

Por ultimo, mediante filename y filemode podremos crear archivos de tipo log.
En filename agregamos el nombre que le daremos a nuestro archivo y en filemode agregamos 'a'
para que los logs que se vayan producionde se agreguen a l final de nuestro archivo.
"""

logging.basicConfig(level=logging.INFO,
                    format="%(processName)s - %(levelname)s - %(asctime)s",
                    filename='Moon.log',
                    filemode="a"
                    )

def suma(numero1: int, numero2: int) -> int:
    """Permite sumar dos numeros enteros.

    Args:
        numero1 (int): 
        numero2 (int):

    Returns:
        int:
    """

    logging.debug('Entramos aqui!')

    resultado = numero1 + numero2

    logging.debug('Nos encontra,ps en esta linea.')

    return resultado

if __name__ == '__main__':
    logging.debug('Ates del llamado de la funcion.')

    resultado = suma(15, 20)
    logging.info(resultado)