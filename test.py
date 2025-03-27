import unittest
from fastapi.testclient import TestClient
from main import app

class TestFastAPIApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})

    def test_get_single_product(self):
        response = self.client.get("/getSingleProduct/test_id")
        self.assertEqual(response.status_code, 200)
        

    def test_get_all_products(self):
        response = self.client.get("/getAll")
        self.assertEqual(response.status_code, 200)
        
if __name__ == "__main__":
    unittest.main()