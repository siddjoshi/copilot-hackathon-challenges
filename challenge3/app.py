from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = [
    {"id": "1", "name": "Laptop", "description": "A high-performance laptop suitable for gaming and work.", "price": 1200.00},
    {"id": "2", "name": "Smartphone", "description": "A latest-generation smartphone with a large display and powerful camera.", "price": 800.00},
    {"id": "3", "name": "Wireless Headphones", "description": "Noise-cancelling wireless headphones with long battery life.", "price": 200.00},
    {"id": "4", "name": "Smartwatch", "description": "A smartwatch with fitness tracking and customizable watch faces.", "price": 150.00},
    {"id": "5", "name": "Tablet", "description": "A lightweight tablet with a sharp display, ideal for reading and browsing.", "price": 300.00}
]

class ItemList(Resource):
    def get(self):
        return jsonify(items)

    def post(self):
        new_item = request.get_json()
        items.append(new_item)
        return new_item, 201

class Item(Resource):
    def get(self, id):
        item = next((item for item in items if item["id"] == id), None)
        if item:
            return jsonify(item)
        return {"message": "Item not found"}, 404

    def put(self, id):
        item = next((item for item in items if item["id"] == id), None)
        if item:
            data = request.get_json()
            item.update(data)
            return jsonify(item)
        return {"message": "Item not found"}, 404

    def delete(self, id):
        global items
        items = [item for item in items if item["id"] != id]
        return {"result": True}

api.add_resource(ItemList, '/api/items')
api.add_resource(Item, '/api/items/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
