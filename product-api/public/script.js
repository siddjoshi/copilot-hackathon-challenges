document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const itemForm = document.getElementById('item-form');
    const formTitle = document.getElementById('form-title');
    const submitBtn = document.getElementById('submit-btn');
    const cancelBtn = document.getElementById('cancel-btn');
    const itemsBody = document.getElementById('items-body');
    const itemId = document.getElementById('item-id');
    const nameInput = document.getElementById('name');
    const descriptionInput = document.getElementById('description');
    const priceInput = document.getElementById('price');
  
    // API URL
    const API_URL = '/api/items';
  
    // Fetch all items
    const getItems = async () => {
      try {
        const response = await fetch(API_URL);
        const data = await response.json();
        
        // Clear table body
        itemsBody.innerHTML = '';
        
        // Add items to table
        data.forEach(item => {
          const row = document.createElement('tr');
          
          row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.description}</td>
            <td>$${parseFloat(item.price).toFixed(2)}</td>
            <td>
              <button class="action-btn edit-btn" data-id="${item._id}">Edit</button>
              <button class="action-btn delete-btn" data-id="${item._id}">Delete</button>
            </td>
          `;
          
          itemsBody.appendChild(row);
        });
        
        // Add event listeners to action buttons
        addActionButtonListeners();
      } catch (error) {
        console.error('Error fetching items:', error);
        alert('Failed to fetch items');
      }
    };
  
    // Add event listeners to action buttons
    const addActionButtonListeners = () => {
      // Edit buttons
      document.querySelectorAll('.edit-btn').forEach(btn => {
        btn.addEventListener('click', () => editItem(btn.getAttribute('data-id')));
      });
      
      // Delete buttons
      document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', () => deleteItem(btn.getAttribute('data-id')));
      });
    };
  
    // Get item by ID
    const getItemById = async (id) => {
      try {
        const response = await fetch(`${API_URL}/${id}`);
        return await response.json();
      } catch (error) {
        console.error('Error fetching item:', error);
        alert('Failed to fetch item details');
        return null;
      }
    };
  
    // Set form to edit mode
    const editItem = async (id) => {
      const item = await getItemById(id);
      
      if (item) {
        // Set form to edit mode
        itemId.value = item._id;
        nameInput.value = item.name;
        descriptionInput.value = item.description;
        priceInput.value = item.price;
        
        formTitle.textContent = 'Edit Product';
        submitBtn.textContent = 'Update Product';
        cancelBtn.style.display = 'inline-block';
      }
    };
  
    // Delete item
    const deleteItem = async (id) => {
      if (confirm('Are you sure you want to delete this product?')) {
        try {
          const response = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
          });
          
          if (response.ok) {
            alert('Product deleted successfully');
            getItems(); // Refresh the list
          } else {
            const data = await response.json();
            alert(`Error: ${data.message || 'Failed to delete product'}`);
          }
        } catch (error) {
          console.error('Error deleting item:', error);
          alert('Failed to delete product');
        }
      }
    };
  
    // Reset form
    const resetForm = () => {
      itemForm.reset();
      itemId.value = '';
      formTitle.textContent = 'Add New Product';
      submitBtn.textContent = 'Add Product';
      cancelBtn.style.display = 'none';
    };
  
    // Form submit handler
    itemForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      // Get form data
      const formData = {
        name: nameInput.value,
        description: descriptionInput.value,
        price: parseFloat(priceInput.value)
      };
      
      // Check if updating or creating
      const isUpdate = itemId.value !== '';
      
      try {
        let response;
        
        if (isUpdate) {
          // Update existing item
          response = await fetch(`${API_URL}/${itemId.value}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
          });
        } else {
          // Create new item
          response = await fetch(API_URL, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
          });
        }
        
        if (response.ok) {
          alert(isUpdate ? 'Product updated successfully' : 'Product added successfully');
          resetForm(); // Reset the form
          getItems(); // Refresh the list
        } else {
          const data = await response.json();
          alert(`Error: ${data.message || 'Failed to process request'}`);
        }
      } catch (error) {
        console.error('Error submitting form:', error);
        alert('Failed to process request');
      }
    });
  
    // Cancel button handler
    cancelBtn.addEventListener('click', resetForm);
  
    // Initial load
    getItems();
  });