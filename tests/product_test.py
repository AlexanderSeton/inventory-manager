import unittest
from models.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("product1", "Test product", 120, 2.50, 3.75)
    
    def test_product_has_name(self):
        self.assertEqual("product1", self.product1.name)
    
    def test_product_has_description(self):
        self.assertEqual("Test product", self.product1.description)

    def test_product_has_stock_quantity(self):
        self.assertEqual(120, self.product1.stock_quantity)

    def test_product_has_buying_cost(self):
        self.assertEqual(2.50, self.product1.buying_cost)

    def test_product_has_selling_cost(self):
        self.assertEqual(3.75, self.product1.selling_price)

    def test_product_has_id(self):
        self.assertEqual(None, self.product1.id)
  