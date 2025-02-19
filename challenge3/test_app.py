import unittest
import json
from app import app, items
 
class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset items to ensure consistent test environment
        items.clear()
        items.extend([
            {"id": "1", "name": "Laptop", "description": "A high-performance laptop suitable for gaming and work.", "price": 1200.00},
            {"id": "2", "name": "Smartphone", "description": "A latest-generation smartphone with a large display and powerful camera.", "price": 800.00},
            {"id": "3", "name": "Wireless Headphones", "description": "Noise-cancelling wireless headphones with long battery life.", "price": 200.00},
            {"id": "4", "name": "Smartwatch", "description": "A smartwatch with fitness tracking and customizable watch faces.", "price": 150.00},
            {"id": "5", "name": "Tablet", "description": "A lightweight tablet with a sharp display, ideal for reading and browsing.", "price": 300.00}
        ])
 
    def test_get_items(self):
        response = self.app.get('/api/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.data)), 5)
 
    def test_get_item(self):
        response = self.app.get('/api/items/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Laptop', str(response.data))
 
    def test_create_item(self):
        new_item = {
            "id": "6",
            "name": "Monitor",
            "description": "A high-resolution monitor.",
            "price": 250.00
        }
        response = self.app.post('/api/items', data=json.dumps(new_item), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Monitor', str(response.data))
 
    def test_update_item(self):
        updated_item = {
            "name": "Updated Laptop",
            "description": "An updated high-performance laptop.",
            "price": 1300.00
        }
        response = self.app.put('/api/items/1', data=json.dumps(updated_item), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Laptop', str(response.data))
 
    def test_delete_item(self):
        response = self.app.delete('/api/items/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['result'], True)
 
if __name__ == "__main__":
    unittest.main()