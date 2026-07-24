
class Product:
    """Класс представления продукта"""

    name:str
    description:str
    price:float
    quantity:int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс подсчета категорий"""

    name:str
    description:str
    products:list

    product_count = 0
    category_count = 0

    def __init__(self, name:str, description:str, products:list[Product]):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products)
        Category.category_count += 1
