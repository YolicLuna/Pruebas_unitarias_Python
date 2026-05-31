from entities.product import Product

# Primero, se define la clase ShopingCart, que representa un carrito de compras.
class ShopingCart:
    
    # El método __init__ se encarga de inicializar el carrito de compras. 
    # En este caso, se crea una lista vacía llamada __products para almacenar los productos que se agregarán al carrito.
    def __init__(self) -> None:
        self.__products:  list[Product] = []

    # Se define una propiedad llamada products, que devuelve una copia de la lista de productos en el carrito.
    # property es un decorador que permite acceder a un método como si fuera un atributo. 
    # En este caso, se devuelve una copia de la lista de productos para evitar que se modifique directamente desde fuera de la clase.
    @property
    def products(self):
        return self.__products.copy()
    
    # Se define otra propiedad llamada total, que calcula el total del carrito de compras.
    @property
    def total(self) -> float:
        return sum( [ (product.price - product.discount) for product in self.__products ] )
        
    # El método add_product se encarga de agregar un producto al carrito de compras.
    def add_product(self, product: Product) -> None:
        self.__products.append(product)
    
    # El método empty se encarga de verificar si el carrito de compras está vacío.
    def empty(self) -> bool:
        return len(self.__products) == 0

    # El método has_products se encarga de verificar si el carrito de compras tiene productos.
    def has_products(self):
        return not self.empty()
    
    # El método remove_product se encarga de eliminar un producto del carrito de compras.
    def remove_product(self, product: Product) -> None:
        self.__products.remove(product)
