import json
from pathlib import Path

from src.Classes import Category, Product


def load_categories_from_json(path: Path) -> list[Category]:
    with open(path) as json_file:
        data = json.load(json_file)
    result = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))

        category_obj = Category(category["name"], category["description"], products)
        result.append(category_obj)

    return result
