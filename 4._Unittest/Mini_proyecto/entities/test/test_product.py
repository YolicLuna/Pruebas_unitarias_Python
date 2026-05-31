import unittest
from entities.product import Product

# Primero, se crea una clase de prueba que herede de unittest.TestCase. 
# Esta clase contendrá los métodos de prueba para la clase Product.
class TestProduct(unittest.TestCase):

    # Este método se ejecuta antes de cada prueba. 
    # Aquí se pueden inicializar objetos o variables que se utilizarán en las pruebas.
    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00

        self.smarthphone = Product(self.name, self.price)

    # Este método prueba la creación de un objeto de tipo Product.
    def test_product_object(self):
        name = 'Manzana'
        price = 10.0

        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, 10.0, 'Lo sentimos, el precio no es el mismo.')

    # Este método prueba el nombre del producto.
    def test_product_name(self):
        self.assertEqual(self.smarthphone.name, self.name)

    # Este método prueba el precio del producto.
    def test_product_price(self):
        self.assertEqual(self.smarthphone.price, self.price)