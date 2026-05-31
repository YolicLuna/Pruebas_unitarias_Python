import unittest
from entities.shopping_cart import ShopingCart
from entities.product import Product
from entities.product import ProductDiscountError

# Esta función se utiliza para determinar si se debe omitir una prueba o no. 
# En este caso, siempre devuelve True, lo que significa que la prueba asociada 
# a esta función se omitirá cada vez que se ejecute el conjunto de pruebas.
def is_avalible_to_skip():
    return True

# Esta función se utiliza para determinar si se debe ejecutar una prueba o no. 
# En este caso, siempre devuelve False, lo que significa que la prueba asociada 
# a esta función se omitirá cada vez que se ejecute el conjunto de pruebas.
def is_conect():
    return False

# Esta clase de prueba unitaria se utiliza para probar la funcionalidad de la clase ShopingCart y la clase Product.
class TestShoppingCart(unittest.TestCase):

    # El método setUpClass se ejecuta una sola vez antes de ejecutar todas las pruebas en la clase TestShoppingCart. 
    # Se utiliza para configurar cualquier recurso compartido o realizar tareas de configuración que solo necesitan hacerse
    # una vez para todas las pruebas.
    # El decorador @classmethod indica que este método es un método de clase, 
    # lo que significa que se puede llamar sin crear una instancia de la clase TestShoppingCart.
    @classmethod
    def setUpClass(cls):
        print('>>> El metodo de clase setUpClass se ejecuta antes de todas las pruebas.')

    # El método tearDownClass se ejecuta una sola vez después de ejecutar todas las pruebas en la clase TestShoppingCart. 
    # Se utiliza para limpiar cualquier recurso compartido o realizar tareas de limpieza que solo necesitan hacerse
    # una vez después de todas las pruebas.
    @classmethod
    def tearDownClass(cls):
        print('>>> El metodo de clase tearDownClass se ejecuta despues de todas las pruebas.')

    # El método setUp se ejecuta antes de cada prueba individual en la clase TestShoppingCart. 
    # Se utiliza para configurar cualquier recurso o realizar tareas de configuración que deben hacerse antes de cada prueba.
    def setUp(self):
        
        # En este método se están creando instancias de la clase Product y la clase ShopingCart,
        # y se están asignando a variables de instancia para que puedan ser utilizadas en las pruebas individuales.
        self.name = 'iPhone'
        self.price = 500.00

        self.smarthphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShopingCart()
        self.shopping_cart_2 = ShopingCart()
        self.shopping_cart_2.add_product(self.smarthphone)

    # El método tearDown se ejecuta después de cada prueba individual en la clase TestShoppingCart. 
    # Se utiliza para limpiar cualquier recurso o realizar tareas de limpieza que deben hacerse después de cada
    # prueba. En este caso, el método tearDown no realiza ninguna acción específica, pero se incluye para mostrar la estructura típica de una clase de prueba unitaria.
    def tearDown(self):
        pass

    # El método test_shopping_cart_empty es una prueba unitaria que verifica si el carrito de compras está vacío.
    # Utiliza el método assertTrue para afirmar que el método empty() del carrito de compras devuelve True, 
    # lo que indica que el carrito está vacío. Si el carrito no está vacío, se muestra un mensaje de error personalizado.
    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos, el carrito de compras no se encuentra vacio. ')

    # El método test_shopping_cart_has_product es una prueba unitaria que verifica si el carrito de compras tiene productos.
    # Utiliza el método assertTrue para afirmar que el método has_products() del carrito de compras devuelve True, 
    # lo que indica que el carrito tiene productos.
    # También utiliza el método assertFalse para afirmar que el método empty() del carrito de compras devuelve False, 
    # lo que indica que el carrito no está vacío. Si el carrito no tiene productos o si el carrito está vacío, se muestra un mensaje de error personalizado.
    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())

    # El método test_product_in_shopping_cart es una prueba unitaria que verifica si un producto específico está presente en el carrito de compras.
    # En esta prueba, se crea un nuevo producto llamado 'Nuevo producto' con un precio de 10 y se agrega al carrito de compras self.shopping_cart_2 utilizando el método add_product.
    # Luego, se utilizan los métodos assertIn para afirmar que el nuevo producto y el producto smarthphone están presentes en la lista de productos del carrito de compras self.shopping_cart_2.
    def test_product_in_shopping_cart(self):

        product = Product('Nuevo producto', 10)
        self.shopping_cart_2.add_product(product)

        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smarthphone, self.shopping_cart_2.products)

    # El método test_remove_product es una prueba unitaria que verifica si un producto específico se puede eliminar del carrito de compras.
    # En esta prueba, se utiliza el método remove_product para eliminar el producto smarthphone del carrito de compras self.shopping_cart_2. 
    # Luego, se utiliza el método assertNotIn para afirmar que el producto smarthphone ya no está presente en la lista de productos del carrito de compras self.shopping_cart_2.
    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smarthphone)
        self.assertNotIn(self.smarthphone, self.shopping_cart_2.products)

    # El método test_discount_error es una prueba unitaria que verifica si se lanza una excepción ProductDiscountError cuando se intenta crear un producto con un descuento mayor al precio del producto.
    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name = 'Laptop', price = 10.0, discount = 11.0)

    # El método test_total_shopping_cart es una prueba unitaria que verifica el cálculo del total del carrito de compras.
    def test_total_shopping_cart(self):

        # En esta prueba, se agregan dos productos al carrito de compras self.shopping_cart_1: un libro con un precio de 15.0 
        # y una cámara con un precio de 700.0 y un descuento de 70.0.
        self.shopping_cart_1.add_product(Product(name='Book', price=15.0))
        self.shopping_cart_1.add_product(Product(name='Camara', price=700.0, discount=70.0))

        self.assertGreater(self.shopping_cart_1.total, 0)
        self.assertLess(self.shopping_cart_1.total, 1000)
        self.assertEqual(self.shopping_cart_1.total, 645.0)

    # El método test_total_empty_shopping_cart es una prueba unitaria que verifica que el total del carrito de compras sea cero cuando el carrito está vacío.
    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0)
    
    # El método test_skip_example es una prueba unitaria que se omite utilizando el decorador @unittest.skip.
    @unittest.skip('La prueba no cumple con los requerimientos.')
    def test_skip_example(self):
        self.assertEqual(1, 1)

    # El método test_skip_example_two es una prueba unitaria que se omite condicionalmente utilizando el decorador @unittest.skipIf.
    @unittest.skipIf(is_avalible_to_skip(), 'No se encuetra con todos los requerimientos.')
    def test_skip_example_two(self):
        pass

    # El método test_skip_example_three es una prueba unitaria que se omite condicionalmente utilizando el decorador @unittest.skipUnless.
    @unittest.skipUnless(is_conect(), 'No se encuetra con todos los requerimientos.')
    def test_skip_example_three(self):
        pass

    # El método test_code_product es una prueba unitaria que verifica si el código del producto coincide con su nombre utilizando una expresión regular.
    def test_code_product(self):
        self.assertRegex(self.smarthphone.code, self.smarthphone.name)

# El bloque if __name__ == '__main__': se utiliza para ejecutar el conjunto de pruebas cuando se ejecuta el archivo directamente.
if __name__ == '__main__':
    unittest.main()
