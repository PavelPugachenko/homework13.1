import pytest

from src.main import Category, Product

@pytest.fixture
def category_with_products():
    product1 = Product("Product1", "Description1", 10, 2)
    product2 = Product("Product2", "Description2", 20, 1)
    category = Category("TestCategory", "Category description", [product1, product2])
    return category

def test_category_total(category_with_products):
    assert category_with_products.gettotalcategory() == 40

def test_category_product_count(category_with_products):
    assert len(category_with_products.products) == 2

def test_product_total():
    product = Product("Product1", "Description1", 10, 5)
    assert product.get_total() == 50

def test_updatequantity():
    obj = YourClass()
    obj.quantity = 5
    assert obj.updatequantity(10) == 10  # Предполагаем, что метод gettotal возвращает значение quantity

