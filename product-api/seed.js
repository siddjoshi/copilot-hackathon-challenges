const mongoose = require('mongoose');
const dotenv = require('dotenv');
const Item = require('./models/Item');

// Load env vars
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('MongoDB connected'))
  .catch(err => {
    console.error('Error connecting to MongoDB:', err);
    process.exit(1);
  });

// Initial data
const items = [
  {
    name: 'Laptop',
    description: 'A high-performance laptop suitable for gaming and work.',
    price: 1200.00
  },
  {
    name: 'Smartphone',
    description: 'A latest-generation smartphone with a large display and powerful camera.',
    price: 800.00
  },
  {
    name: 'Wireless Headphones',
    description: 'Noise-cancelling wireless headphones with long battery life.',
    price: 200.00
  },
  {
    name: 'Smartwatch',
    description: 'A smartwatch with fitness tracking and customizable watch faces.',
    price: 150.00
  },
  {
    name: 'Tablet',
    description: 'A lightweight tablet with a sharp display, ideal for reading and browsing.',
    price: 300.00
  }
];

// Import data
const importData = async () => {
  try {
    await Item.deleteMany();
    console.log('Data cleared...');
    
    await Item.insertMany(items);
    console.log('Data imported!');
    
    process.exit();
  } catch (err) {
    console.error('Error importing data:', err);
    process.exit(1);
  }
};

// Run import
importData();