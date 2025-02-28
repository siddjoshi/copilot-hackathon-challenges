# Challenge 3 – API Development and CRUD Operations

> **Note:** You can use any programming language you're comfortable with for this challenge. The following Java-based instructions are just for illustration. Feel free to adapt the setup and implementation steps according to your chosen technology stack.

## Setup Steps

### 1. Setup Your Development Environment

#### For Java:
- Ensure you have the Java Development Kit (JDK) installed. You'll need JDK 8 or higher.
- Verify installation by running `java -version` and `javac -version` in your terminal. This should return the installed versions.

#### Choose an Integrated Development Environment (IDE):
- Use IntelliJ IDEA, or Visual Studio Code (with Java support and Copilot enabled).

#### Set Up Maven or Gradle:
- Maven and Gradle are build automation tools that help manage project dependencies.
- Install Maven or Gradle if they aren't already installed.
- Set up your project as a Maven or Gradle project in your IDE. This will create the necessary project structure.

#### For Python:
- Ensure you have Python installed. You'll need Python 3.6 or higher.
- Verify installation by running `python --version` in your terminal. This should return the installed version.
- Set up a virtual environment by running `python -m venv venv`.
- Activate the virtual environment:
  - On Windows: `venv\Scripts\activate`
  - On macOS/Linux: `source venv/bin/activate`
- Install the necessary dependencies using `pip install -r requirements.txt`.

#### For Other Languages:
- Set up the development environment for your chosen language
- Install the necessary runtime and development tools
- Choose an IDE or code editor that supports your language and has Copilot enabled

### 2. Create a New Project
- Create a new project using your preferred language and framework
- Set up the project structure according to the best practices of your chosen technology

### 3. Add Required Dependencies
- Add the necessary dependencies for:
  - Web/HTTP server functionality
  - JSON handling
  - Your preferred web framework
  - Any additional libraries needed for your implementation

#### Spring Boot:
- Add Spring Boot, a framework for building RESTful APIs in Java.
- For Maven, add the `spring-boot-starter-web` dependency to your `pom.xml`.
- Spring Boot simplifies application development by providing pre-configured templates.

### 4. Create the Model Class for the Following JSON

```json
[
    {
        "id": "1",
        "name": "Laptop",
        "description": "A high-performance laptop suitable for gaming and work.",
        "price": 1200.00
    },
    {
        "id": "2",
        "name": "Smartphone",
        "description": "A latest-generation smartphone with a large display and powerful camera.",
        "price": 800.00
    },
    {
        "id": "3",
        "name": "Wireless Headphones",
        "description": "Noise-cancelling wireless headphones with long battery life.",
        "price": 200.00
    },
    {
        "id": "4",
        "name": "Smartwatch",
        "description": "A smartwatch with fitness tracking and customizable watch faces.",
        "price": 150.00
    },
    {
        "id": "5",
        "name": "Tablet",
        "description": "A lightweight tablet with a sharp display, ideal for reading and browsing.",
        "price": 300.00
    }
]
```

### 5. Implement Data Operations
a. Read and Write to the JSON file 
b. Alternatively, you can use a database for data storage

### 6. Create REST API Endpoints
Implement the following CRUD operations:
- GET /api/items: Retrieve all items
- GET /api/items/{id}: Retrieve an item by its ID
- POST /api/items: Create a new item
- PUT /api/items/{id}: Update an existing item
- DELETE /api/items/{id}: Delete an item

### 7. Add Exception Handling
Implement proper error handling for your API endpoints

## Improve UI
1. Display the data in table format on UI
2. Implement CRUD operations through the UI

## Add Test Cases
1. Write test cases for the GET, POST, PUT and DELETE operations
2. Include edge cases and null conditions
3. Run the test cases
