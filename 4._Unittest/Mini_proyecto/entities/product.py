
# Primero, definamos una clase de excepción personalizada para manejar errores relacionados con el descuento del producto.
class ProductDiscountError(Exception):
    pass

# Ahora, definamos la clase Product con sus atributos y métodos.
class Product:
    
    # El constructor de la clase Product recibe el nombre, el precio y un descuento opcional. 
    # Si el descuento es mayor que el precio, se lanza una excepción.
    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price

        if discount > price:
            raise ProductDiscountError('Lo sentimos el descuento no puede ser mayor al precio.')

        self.discount = discount

    # El método get_price devuelve el precio del producto después de aplicar el descuento.
    @property
    def code(self):
        return f'code-{self.name}'