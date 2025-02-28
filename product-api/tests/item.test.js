const mongoose = require('mongoose');
const request = require('supertest');
const app = require('../app');
const Item = require('../models/Item');
const connectDB = require('../config/db');

// Connect to test database before running tests
beforeAll(async () => {
  await connectDB();
});

// Clear the database after each test
afterEach(async () => {
  await Item.deleteMany();
});

// Close database connection after all tests
afterAll(async () => {
  await mongoose.connection.close();
});

describe('Item API', () => {
  // Test item data
  const testItem = {
    name: 'Test Item',
    description: 'This is a test item',
    price: 99.99
  };

  // Test for GET /api/items
  describe('GET /api/items', () => {
    it('should get all items', async () => {
      // Create test items
      await Item.create(testItem);
      await Item.create({
        name: 'Another Item',
        description: 'Another test item',
        price: 49.99
      });

      const res = await request(app)
        .get('/api/items');
      
      expect(res.statusCode).toEqual(200);
      expect(Array.isArray(res.body)).toBeTruthy();
      expect(res.body.length).toEqual(2);
    });

    it('should return empty array when no items exist', async () => {
      const res = await request(app)
        .get('/api/items');
      
      expect(res.statusCode).toEqual(200);
      expect(Array.isArray(res.body)).toBeTruthy();
      expect(res.body.length).toEqual(0);
    });
  });

  // Test for GET /api/items/:id
  describe('GET /api/items/:id', () => {
    it('should get a specific item by ID', async () => {
      const item = await Item.create(testItem);

      const res = await request(app)
        .get(`/api/items/${item._id}`);
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.name).toEqual(testItem.name);
      expect(res.body.description).toEqual(testItem.description);
      expect(res.body.price).toEqual(testItem.price);
    });

    it('should return 404 if item not found', async () => {
      const nonExistentId = new mongoose.Types.ObjectId();
      
      const res = await request(app)
        .get(`/api/items/${nonExistentId}`);
      
      expect(res.statusCode).toEqual(404);
      expect(res.body.message).toEqual('Item not found');
    });

    it('should return 404 for invalid ID format', async () => {
      const res = await request(app)
        .get('/api/items/invalidid');
      
      expect(res.statusCode).toEqual(404);
      expect(res.body.message).toEqual('Item not found - Invalid ID');
    });
  });

  // Test for POST /api/items
  describe('POST /api/items', () => {
    it('should create a new item', async () => {
      const res = await request(app)
        .post('/api/items')
        .send(testItem);
      
      expect(res.statusCode).toEqual(201);
      expect(res.body.name).toEqual(testItem.name);
      expect(res.body.description).toEqual(testItem.description);
      expect(res.body.price).toEqual(testItem.price);
      
      // Verify item was saved to database
      const items = await Item.find();
      expect(items.length).toEqual(1);
    });

    it('should return 400 for missing required fields', async () => {
      const res = await request(app)
        .post('/api/items')
        .send({ name: 'Incomplete Item' });
      
      expect(res.statusCode).toEqual(400);
      
      // Verify no item was saved
      const items = await Item.find();
      expect(items.length).toEqual(0);
    });

    it('should return 400 for negative price', async () => {
      const res = await request(app)
        .post('/api/items')
        .send({
          name: 'Negative Price Item',
          description: 'This item has a negative price',
          price: -10
        });
      
      expect(res.statusCode).toEqual(400);
      
      // Verify no item was saved
      const items = await Item.find();
      expect(items.length).toEqual(0);
    });
  });

  // Test for PUT /api/items/:id
  describe('PUT /api/items/:id', () => {
    it('should update an existing item', async () => {
      const item = await Item.create(testItem);
      
      const updatedData = {
        name: 'Updated Item',
        description: 'This item has been updated',
        price: 149.99
      };
      
      const res = await request(app)
        .put(`/api/items/${item._id}`)
        .send(updatedData);
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.name).toEqual(updatedData.name);
      expect(res.body.description).toEqual(updatedData.description);
      expect(res.body.price).toEqual(updatedData.price);
      
      // Verify item was updated in database
      const updatedItem = await Item.findById(item._id);
      expect(updatedItem.name).toEqual(updatedData.name);
    });

    it('should return 404 if item not found', async () => {
      const nonExistentId = new mongoose.Types.ObjectId();
      
      const res = await request(app)
        .put(`/api/items/${nonExistentId}`)
        .send(testItem);
      
      expect(res.statusCode).toEqual(404);
      expect(res.body.message).toEqual('Item not found');
    });
  });

  // Test for DELETE /api/items/:id
  describe('DELETE /api/items/:id', () => {
    it('should delete an existing item', async () => {
      const item = await Item.create(testItem);
      
      const res = await request(app)
        .delete(`/api/items/${item._id}`);
      
      expect(res.statusCode).toEqual(200);
      expect(res.body.message).toEqual('Item removed');
      
      // Verify item was deleted from database
      const deletedItem = await Item.findById(item._id);
      expect(deletedItem).toBeNull();
    });

    it('should return 404 if item not found', async () => {
      const nonExistentId = new mongoose.Types.ObjectId();
      
      const res = await request(app)
        .delete(`/api/items/${nonExistentId}`);
      
      expect(res.statusCode).toEqual(404);
      expect(res.body.message).toEqual('Item not found');
    });
  });
});