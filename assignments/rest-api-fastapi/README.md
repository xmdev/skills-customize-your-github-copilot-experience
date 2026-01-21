# 📘 Assignment: REST API with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to learn modern web API development, HTTP methods, request/response handling, and data validation.

## 📝 Tasks

### 🛠️ Create a Book Library API

#### Description
Build a REST API that manages a collection of books. The API should support creating, reading, updating, and deleting book records.

#### Requirements
Completed program should:

- Implement GET endpoint to retrieve all books
- Implement GET endpoint to retrieve a single book by ID
- Implement POST endpoint to add a new book
- Implement PUT endpoint to update an existing book
- Implement DELETE endpoint to remove a book
- Use Pydantic models for request/response validation
- Include proper HTTP status codes (200, 201, 404, etc.)
- Store data in memory (list or dictionary)

### 🛠️ Add Search and Filtering

#### Description
Extend your API with query parameters to search and filter books by different criteria.

#### Requirements
Completed program should:

- Add query parameter to filter books by author
- Add query parameter to filter books by genre
- Add query parameter to search books by title (partial match)
- Return appropriate results or empty list when no matches found
- Handle multiple filters simultaneously
