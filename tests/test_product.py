import pytest
from src.main import Product, product1, product2, product3
from src.main import Category
import unittest


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5

def test_product_price_type(product_1):
    # Проверяем, что цена имеет правильный тип данных
    assert type(product_1.price) == float

def test_product_quantity_type(product_1):
    # Проверяем, что количество имеет правильный тип данных
    assert type(product_1.quantity) == int

class TestProduct(unittest.TestCase):

    def setUp(self):
        """Выполняется перед каждым тестом, создает экземпляр Product."""
        self.product = Product("Test Product", "Test Description", 100.0, 10)

    def test_product_creation(self):
        """Проверяет, что экземпляр Product создается правильно."""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "Test Description")
        self.assertEqual(self.product.price, 100.0)
        self.assertEqual(self.product.quantity, 10)

    def test_product_name(self):
        """Проверяет, что имя продукта можно получить."""
        self.assertEqual(self.product.name, "Test Product")

    def test_product_price(self):
        """Проверяет, что цена продукта соответствует ожидаемой."""
        self.assertEqual(self.product.price, 100.0)

    def test_product_quantity(self):
        """Проверяет, что количество продукта соответствует ожидаемому."""
        self.assertEqual(self.product.quantity, 10)

    def test_product_type(self):
        """Проверяет, что атрибуты имеют правильный тип данных"""
        self.assertIsInstance(self.product.name, str)
        self.assertIsInstance(self.product.description, str)
        self.assertIsInstance(self.product.price, float)
        self.assertIsInstance(self.product.quantity, int)



@pytest.fixture
def category_1():
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни", [product1, product2, product3])

def test_init_2(category_1):

     assert category_1.name == "Смартфоны"
     assert category_1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
     assert category_1.products == [product1, product2, product3]



class TestCategory(unittest.TestCase):

    def setUp(self):
        """
        Создаем тестовые данные для использования в тестах.
        Выполняется перед каждым тестом.
        """
        Category.category_count = 0
        Category.product_count = 0
        self.product1 = Product("Товар 1", "Описание 1", 100.0, 5)
        self.product2 = Product("Товар 2", "Описание 2", 200.0, 10)
        self.category = Category("Тестовая категория", "Описание категории", [self.product1, self.product2])

    def test_category_creation(self):
        """Проверяем корректность создания экземпляра Category."""
        self.assertEqual(self.category.name, "Тестовая категория")
        self.assertEqual(self.category.description, "Описание категории")
        self.assertEqual(len(self.category.products), 2)
        self.assertEqual(Category.category_count, 1)  # Проверяем счетчик категорий
        self.assertEqual(Category.product_count, 2)   # Проверяем счетчик товаров

    def test_category_attributes(self):
        """Проверяем атрибуты экземпляра Category."""
        self.assertEqual(self.category.name, "Тестовая категория")
        self.assertEqual(self.category.description, "Описание категории")
        self.assertEqual(self.category.products, [self.product1, self.product2])

    def test_category_count(self):
        """Проверяем счетчик категорий при создании новых экземпляров."""
        category2 = Category("Категория 2", "Описание 2",  [])
        self.assertEqual(Category.category_count, 2)

    def test_product_count(self):
        """Проверяем счетчик товаров при создании новых категорий."""
        category2 = Category("Категория 2", "Описание 2", [self.product1])
        self.assertEqual(Category.product_count, 3)