import unittest
import requests

class TestProductsAPI(unittest.TestCase):
    BASE_URL = "https://fakestoreapi.com"

    def test_get_all_products(self):
        response = requests.get(f"{self.BASE_URL}/products")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), list))

    def test_get_invalid_product(self):
        response = requests.get(f"{self.BASE_URL}/products/99999")
        self.assertIn(response.status_code, [404, 200])  # Depends on API behavior
