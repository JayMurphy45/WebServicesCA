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
        response = self.client.get("/getSingleProduct/AUTO008")
        self.assertEqual(response.status_code, 200)
        

    def test_get_all_products(self):
        response = self.client.get("/getAll")
        self.assertEqual(response.status_code, 200)

    def test_add_new(self):
        response = self.client.post("/addNew/AUTO008/Motor/1.0/1/test")
        self.assertEqual(response.status_code, 200)
    
    def test_delete_one(self):
        response = self.client.delete("/deleteOne/AUTO008")
        self.assertEqual(response.status_code, 200)
    
    def test_starts_with(self):
        response = self.client.get("/startsWith/m")
        self.assertEqual(response.status_code, 200)
    
    def test_paginate(self):
        response = self.client.get("/paginate/1/2")
        self.assertEqual(response.status_code, 200)
    
    def test_convert(self):
        response = self.client.get("/convert/AUTO008")
        self.assertEqual(response.status_code, 200)
    

        
if __name__ == "__main__":
    unittest.main()