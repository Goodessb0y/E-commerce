import json

from src.Classes import Category, Product
from src.utils import load_categories_from_json


def test_load_categories_from_json(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Телефоны",
            "products": [
                {
                    "name": "Samsung S25",
                    "description": "Флагман",
                    "price": 120000,
                    "quantity": 5,
                },
                {
                    "name": "iPhone 17",
                    "description": "Apple",
                    "price": 150000,
                    "quantity": 3,
                },
            ],
        }
    ]

    file = tmp_path / "test.json"

    with open(file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file)

    result = load_categories_from_json(file)

    assert len(result) == 1

    assert isinstance(result[0], Category)

    assert result[0].name == "Смартфоны"
    assert result[0].description == "Телефоны"

    products = result[0].products

    assert isinstance(products, str)
    assert "Samsung S25, 120000 руб. Остаток: 5 шт.\n" in products
    assert "iPhone 17, 150000 руб. Остаток: 3 шт.\n" in products
    assert len(products.splitlines()) == 2
