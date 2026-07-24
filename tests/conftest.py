import pytest

from src.Classes import Category, Product


@pytest.fixture
def product():
    product = Product("Samsung S 25", "Лучший выбор", 120999.99, 16)
    return product


@pytest.fixture
def category():
    product_1 = Product("Samsung S 25", "Лучший выбор", 120999.99, 16)
    product_2 = Product("Iphone 17 Pro Max", "It`s revolution Johny!", 170299.99, 4)
    product_3 = Product("Realmi C14", "Chig Chong, Ping Pong", 69000, 25)
    p_list = [product_1, product_2, product_3]
    category = Category("Смартфон", "Флагманы 2026", p_list)

    return category
