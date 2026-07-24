from src.Classes import Category, Product


def test_product_init(product):
    assert product.name == "Samsung S 25"
    assert product.description == "Лучший выбор"
    assert product.price == 120999.99
    assert product.quantity == 16


def test_category_init(category):
    assert category.name == 'Смартфон'
    assert category.description == 'Флагманы 2026'
    assert len(category.products) == 3




def test_category_count():
    Category.category_count = 0
    product_4 = Product('Ariston', 'Мороз по коже', 25000, 5)
    product_5 = Product('LG', 'Генератор снега', 31999, 8)
    p_list_2 = [product_4, product_5]

    product_6 = Product('Молоток', 'Сделано в СССР', 3560, 56)
    product_7 = Product('Пила', 'Зубчатая', 1590, 49)
    p_list_3 = [product_6, product_7]

    data_test_1 = Category('Бытовая техника', 'Для кухни', p_list_2)
    data_test_2 = Category('Инструмент', 'Для дома', p_list_3)
    assert Category.category_count == 2


def test_product_count():
    Category.product_count = 0
    product_4 = Product('Ariston', 'Мороз по коже', 25000, 5)
    product_5 = Product('LG', 'Генератор снега', 31999, 8)
    p_list_2 = [product_4, product_5]

    product_6 = Product('Молоток', 'Сделано в СССР', 3560, 56)
    product_7 = Product('Пила', 'Зубчатая', 1590, 49)
    p_list_3 = [product_6, product_7]

    data_test_1 = Category('Бытовая техника', 'Для кухни', p_list_2)
    data_test_2 = Category('Инструмент', 'Для дома', p_list_3)
    assert Category.product_count == 4