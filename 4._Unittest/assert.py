"""
Assert es una palabra reservada que nos permite evaluar una condicion, si la 
condicion se cumple entonces el programa continua con su ejecucion, de lo contrario,
un error/excepcion sera lanzado. 
"""
"""
En este primer ejemplo, se ejecuta una condicion que si se cumple, 10 es igual a 10,
por lo tanto el programa continua y se imprime '>>> El programa continua con su ejecucion.'.
"""

if __name__ == '__main__':
    assert 10 == 10

    print('>>> El programa continua con su ejecucion.')



"""
En este segundo ejemplo la condicion no se cumple ya que 5 no es igual a 10,
asi que el programa lanza una excepcion AssertionError junto con el mensaje 
'Lo sentimos, cinco no es igual a 10.'.
"""

if __name__ == '__main__':
    assert 5 == 10, 'Lo sentimos, cinco no es igual a 10.'

    print('>>> El programa continua con su ejecucion.')



"""
Lo interesante de conocer el error es que nosotros podemos manejarlo.
Como en este tercer ejemplo, en elque utilizamos un try y except con el erro
AssertionError como error e imprimimos error.
"""

if __name__ == '__main__':
    try:
        assert 5 == 10, 'Lo sentimos, cinco no es igual a 10.'
        print('>>> El programa continua con su ejecucion.')

    except AssertionError as error:
        print(error)


"""
En este ultimo ejemplo se define una funcion que solo debe sumar numeros enteros,
contiene su propio docstring y se aplica un assert en caso de que los numeros sean negativos,
con su respectivo mensaje de error. 
"""

def suma_numeros_positivos(n1: int, n2: int) -> int:
    """Permite sumar dos numeros enteros positivos.

    Args:
        n1 (int): 
        n2 (int):

    Returns:
        int:
    """

    assert n1 > 0 and n2 > 0, "Lo sentimos, solo es posible sumar numeros enteros positivos."

    return n1 + n2

if __name__ == '__main__':
    resultado = suma_numeros_positivos(10, 20)
    print(resultado)