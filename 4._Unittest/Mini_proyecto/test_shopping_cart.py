import unittest
from shopping_cart import ShopingCart
from product import Product
from product import ProductDiscountError

def is_avalible_to_skip():
    return True

def is_conect():
    return False

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

    def test_product_in_shopping_cart(self):

        product = Product('Nuevo producto', 10)
        self.shopping_cart_2.add_product(product)

        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smarthphone, self.shopping_cart_2.products)

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smarthphone)
        self.assertNotIn(self.smarthphone, self.shopping_cart_2.products)

    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name = 'Laptop', price = 10.0, discount = 11.0)

    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Book', price=15.0))
        self.shopping_cart_1.add_product(Product(name='Camara', price=700.0, discount=70.0))

        self.assertGreater(self.shopping_cart_1.total, 0)
        self.assertLess(self.shopping_cart_1.total, 1000)
        self.assertEqual(self.shopping_cart_1.total, 645.0)

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0)
    
    @unittest.skip('La prueba no cumple con los requerimientos.')
    def tets_skip_example(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(is_avalible_to_skip(), 'No se encuetra con todos los requerimientos.')
    def test_skip_example_two(self):
        pass

    @unittest.skipUnless(is_conect(), 'No se encuetra con todos los requerimientos.')
    def test_skip_example_three(self):
        pass



if __name__ == '__main__':
    unittest.main()
