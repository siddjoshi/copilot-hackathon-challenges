const mongoose = require('mongoose');

const itemSchema = mongoose.Schema(
  {
    name: {
      type: String,
      required: [true, 'Please add a name']
    },
    description: {
      type: String,
      required: [true, 'Please add a description']
    },
    price: {
      type: Number,
      required: [true, 'Please add a price'],
      min: [0, 'Price cannot be negative']
    }
  },
  {
    timestamps: true
  }
);

module.exports = mongoose.model('Item', itemSchema);