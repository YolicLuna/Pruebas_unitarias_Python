import pytest

"""
Para que nuestras pruebas funciones, el nombre de nuestras funciones siempre deben
comenzar con el prefijo tes_. 
De igual manera, todo va a funcionar mediante la palabra reservada assert.
Recordemos que assert lanza una excepcion en caso de que la condicion no se cumpla.

En consola, encontrandote en la ubicacion correcta, que seria la carpeta 5._Pytest,
basta con ejecutar el comando pytest para que corran todas las pruebas que existan 
dentro de todos los archivos, aclarando que solo se ejecutaran aquellas que tenan el prefijo test_
al inicio del nombre.

Al ejecutar pytest, lo primero que se mostrara algo como "test_main.py ..F." y en esa respuesta
cada punto indica una prueba que paso y las F es una prueba fallida.
Al final se mostrara algo como  "1 failed, 3 passed in 0.08s", que indica las pruebas que fallaron y las que pasaron.
Y en medio de esas dos pruebas, se muestran las excepciones de las pruebas que no pasaron junto al mensaje 
de error que agreguemos, en caso de hacerlo, claro esta.
"""

def test_example():
    assert 10 == 10

"""
Recordemos que lo mejor es agrupar las pruebas mediante una clase, o sea, cada prueba
debe ser un metodo de una clase.
La clase obligatoriamente debe comenzar su nombre con Test, ya que de no ser asi, pytest no tomara esa
clase como una clase de prueba y la ignorara, por lo tanto no ejecutara las pruebas, metodos dentro de esa clase.
"""

"""
Podemos especificar la prueba que queremos que se eejcute evitando las demas.
Seria ejecutando en consola, por ejemplo, "pytest test_main.py::TestExample::test_resta_dos_numeros"
El contenido de este comando es el coando pytest, segudi del archivo que contiene las pruebas, seguido del nombre
de las clase que contiene el metodo/prueba a ejecutar y el nombre de metodo/prueba a ejecutar.
Y por supuesto, para ejecutar todas las pruebas pero de una sola clase, ejecutamos el mismo comando pero
sin colocar el nombre del metodo/prueba.
"""

class TestExample():

    def test_suma_dos_numeros(self):
        assert 10 + 10 == 20

    #Podemos agrear un mensaje para que se muestre en caso la condicion no se cumpla.
    def test_resta_dos_numeros(self):
        assert 30 - 10 == 20, 'Lo sentimos, la resta no es correcta'
    

class TestExample2():

    def test_multiplica_dos_numeros(self):
        assert 10 * 10 == 100

"""
Al igual que unittest, todoas las pruebas se ejecutan de manera individual, es decir,
ninguna depende de otra ni se obstruyen. Por lo que puede ser que en ocasiones sea necesario 
realizar ciertas acciones antes y despues de cada prueba. 
Y al igual que con unittest, utilizaremos setUp y tearDown.

Al ejecutar solo 'pytest' en consola, los print no se visualizaran, para ello debemos agregar
'-s' despues de pytest, en tonces, en consola deberemos ejecutar 'pytest -s'.

Si queremos que los metodos setup y teardown se ejecuten a nivel de clase, es decir, antes y despues
de que se ejcuten todas las pruebas de esa clase, deberemo agregar los metodos setup y teardown
pero con el decorador @classmethod.
"""

class TestExample3():

    @classmethod
    def setup_class(cls):
        print('>>> setup_class se ejecutan antes de todas las pruebas.')

    @classmethod
    def teardow_clas(cls):
        print('>>> teardown_class se ejecutan despues de todas las pruebas.')

    def setup_method(self):
        self.numero_uno = 10
        self.numero_dos = 20

    def teardown_method(self):
        print('>>> El metodo teardown se ejecuta despues de cada prueba.')

    def test_suma_dos_numeros(self):
        assert self.numero_uno + self.numero_dos == 30


