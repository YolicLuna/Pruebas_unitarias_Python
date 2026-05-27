import unittest
from entities.product import Product

class TetsProduct(unittest.TestCase):

    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00

        self.smarthphone = Product(self.name, self.price)

    def test_product_object(self):
        name = 'Manzana'
        price = 10.0

        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, 10.0, 'Lo sentimos, el precio no es el mismo.')

    def test_product_name(self):
        self.assertEqual(self.smarthphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smarthphone.price, self.price)