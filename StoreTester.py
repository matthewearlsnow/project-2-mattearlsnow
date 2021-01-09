# Author: Matthew Snow
# Date: January 8, 2021
# Description: Unit Testing

import unittest
import Store

class Test_Store(unittest.TestCase):
    def test_Product(self):
        p1 = Store.Product("999", "The Vow", "We are one", 44, 3)
        results = p1.get_product_id()
        self.assertIsNotNone(results)

class Test_Customer(unittest.TestCase):
    def test_Customer(self):
        c1 = Store.Customer("Matt", "MES", True)
        results = c1.is_premium_member()
        self.assertTrue(results)


class Test_Product_two(unittest.TestCase):
    def test_Product_two(self):
        p1 = Store.Product("999", "The Vow", "We are one", 44, 3)
        results = p1.get_price()
        self.assertGreater(results, 0)




if __name__=="__main__":
    unittest.main()
