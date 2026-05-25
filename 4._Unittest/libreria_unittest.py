"""
Importamos unittest.
Unittest ya se encuentra en la biblioteca estandar de Python.
Asi que no debemos instalar nda, solo importar.
"""

import unittest

"""
Ahora, vamos a definir unas pruebas unitarias utilizando metodos,
asi que vamos a crear una nueva clase.
Todas las clases de prueba deben comenzar con Test en su nombre, sea cual sea,
ejemplo, TestExample, esto pasar identificar cuales son clases de testing.

Es importante saber que todos los metodos que hagan referiencia a una prueba
obligatoriamente deben comenzar con el prefijo test_.

assertEqual evalua que el resultado se igual al esperado, en el caso de nuestro ejemplo,
se evalua que el resultado sea igual a 30.

main, en unittest, ejecuta todos los metodos que tengan el prefijo test_ 
que se encuentren en las clases que hereden de TestCase
"""

class TestExample(unittest.TestCase): #Se crea la clase Example y hereda de TestCase.

    def test_suma_numeros(self): #se define un metodo con el prefijo test_
        numero1 = 10
        numero2 = 20

        resultado = numero1 + numero2

        self.assertEqual(resultado, 30) #Se evalua que el resultado sea igual a 30

    def test_resta_numeros(self):
        self.assertEqual( 30 - 20, 10)

if __name__ == '__main__':
    unittest.main() 
