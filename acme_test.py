import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    def test_default_steal_explode(self):
        """Test default stealability and explode"""
        prod = Product('Test Product 2')
        self.assertEqual(prod.stealability(), 'Kinda stealable...')
        self.assertEqual(prod.explode(), '...fizzle.')
        
class AcmeReportTests(unittest.TestCase):
    """Make sure you can impress Sr. Data Scientists"""

    def setUp(self):
        """Set up tests methods"""
        self.products = generate_products()

    def test_default_num_products(self):
        """confirm default for Products is 30"""
        self.assertEqual(len(self.products), 30)

    def test_legal_names(self):
        """make sure product names are part of list"""
        for product in self.products:
            name = product.name.split()
            self.assertIn(name[0], ADJECTIVES)
            self.assertIn(name[1], NOUNS)

if __name__ == '__main__':
    unittest.main()