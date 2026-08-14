class Product:
    """Класс представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product_data: dict, existing_products):
        for prod in existing_products:
            if prod.name == product_data['name']:
                prod.quantity += product_data['quantity']
                prod.price = max(prod.price,product_data['price'])
                return prod
        return cls(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, price):
        if price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        elif price < self.__price:
            answer = input('Предложенная цена ниже действующей, обновить?')
            if answer.lower() == 'y':
                self.__price = price
        else:
            self.__price = price

class Category:
    """Класс подсчета категорий"""

    name: str
    description: str
    products: list

    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return result


    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1


