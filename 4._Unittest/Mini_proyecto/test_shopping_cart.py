import unittest
from shopping_cart import ShopingCart
from product import Product

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>>> El metodo de clase setUpClass se ejecuta antes de todas las pruebas.')

    @classmethod
    def tearDownClass(cls):
        print('>>> El metodo de clase tearDownClass se ejecuta despues de todas las pruebas.')

    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00

        self.smarthphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShopingCart()
        self.shopping_cart_2 = ShopingCart()
        self.shopping_cart_2.add_product(self.smarthphone)

    def tearDown(self):
        pass

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

    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos, el carrito de compras no se encuentra vacio. ')

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())

if __name__ == '__main__':
    unittest.main()
