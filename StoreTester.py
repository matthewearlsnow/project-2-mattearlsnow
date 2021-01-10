# Author: Matthew Snow
# Date: January 8, 2021
# Description: This is for unit testing.

import unittest
import Store

class Test_Store(unittest.TestCase):
    """Assert product ID is not None"""
    def test_Product(self):
        p1 = Store.Product("999", "The Vow", "We are one", 44, 3)
        results = p1.get_product_id()
        self.assertIsNotNone(results)

class Test_Customer(unittest.TestCase):
    """Assert customer is premium member is true test"""
    def test_Customer(self):
        c1 = Store.Customer("Matt", "MES", True)
        results = c1.is_premium_member()
        self.assertTrue(results)

class Test_Product_price(unittest.TestCase):
    """Assert product price is great than 0 """
    def test_Product_price(self):
        p1 = Store.Product("999", "The Vow", "We are one", 44, 3)
        results = p1.get_price()
        self.assertGreater(results, 0)

class Test_Product(unittest.TestCase):
    """Assert get product ID is true test"""
    def test_Product(self):
        p1 = Store.Product("999", "The Vow", "We are one", 44, 3)
        results = p1.get_product_id()
        self.assertTrue(results)

class Test_decrease_quantity(unittest.TestCase):
    """Decrease/Assert is less - amount test"""
    def test_decrease(self):
        p1 = Store.Product("999", "The Vow", "We are one", 44, 3)
        quantity = p1.get_quantity_available()
        p1.decrease_quanity()
        results = p1.get_quantity_available()
        self.assertLess(results, quantity)


if __name__=="__main__":
    unittest.main()
