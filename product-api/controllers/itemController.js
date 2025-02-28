const Item = require('../models/Item');

// @desc    Get all items
// @route   GET /api/items
// @access  Public
const getItems = async (req, res) => {
  try {
    const items = await Item.find();
    res.status(200).json(items);
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
};

// @desc    Get single item
// @route   GET /api/items/:id
// @access  Public
const getItem = async (req, res) => {
  try {
    const item = await Item.findById(req.params.id);
    
    if (!item) {
      return res.status(404).json({ message: 'Item not found' });
    }
    
    res.status(200).json(item);
  } catch (error) {
    if (error.kind === 'ObjectId') {
      return res.status(404).json({ message: 'Item not found - Invalid ID' });
    }
    res.status(500).json({ message: error.message });
  }
};

// @desc    Create a new item
// @route   POST /api/items
// @access  Public
const createItem = async (req, res) => {
  try {
    const { name, description, price } = req.body;
    
    // Validation
    if (!name || !description || !price) {
      return res.status(400).json({ message: 'Please provide name, description, and price' });
    }
    
    // Create item
    const item = await Item.create({
      name,
      description,
      price
    });
    
    res.status(201).json(item);
  } catch (error) {
    res.status(400).json({ message: error.message });
  }
};

// @desc    Update an item
// @route   PUT /api/items/:id
// @access  Public
const updateItem = async (req, res) => {
  try {
    const { name, description, price } = req.body;
    
    // Find item
    let item = await Item.findById(req.params.id);
    
    if (!item) {
      return res.status(404).json({ message: 'Item not found' });
    }
    
    // Update item
    item = await Item.findByIdAndUpdate(
      req.params.id,
      { name, description, price },
      { new: true, runValidators: true }
    );
    
    res.status(200).json(item);
  } catch (error) {
    if (error.kind === 'ObjectId') {
      return res.status(404).json({ message: 'Item not found - Invalid ID' });
    }
    res.status(400).json({ message: error.message });
  }
};

// @desc    Delete an item
// @route   DELETE /api/items/:id
// @access  Public
const deleteItem = async (req, res) => {
  try {
    const item = await Item.findById(req.params.id);
    
    if (!item) {
      return res.status(404).json({ message: 'Item not found' });
    }
    
    await Item.findByIdAndDelete(req.params.id);
    
    res.status(200).json({ message: 'Item removed' });
  } catch (error) {
    if (error.kind === 'ObjectId') {
      return res.status(404).json({ message: 'Item not found - Invalid ID' });
    }
    res.status(500).json({ message: error.message });
  }
};

module.exports = {
  getItems,
  getItem,
  createItem,
  updateItem,
  deleteItem
};