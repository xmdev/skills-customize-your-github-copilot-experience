from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# TODO: Define your Book model using Pydantic BaseModel
# Example structure:
# class Book(BaseModel):
#     id: int
#     title: str
#     author: str
#     genre: str
#     year: int

# TODO: Create an in-memory storage for books
books = []

# TODO: Implement GET /books endpoint to retrieve all books
@app.get("/books")
def get_books():
    pass

# TODO: Implement GET /books/{book_id} endpoint to retrieve a single book
@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass

# TODO: Implement POST /books endpoint to create a new book
@app.post("/books")
def create_book():
    pass

# TODO: Implement PUT /books/{book_id} endpoint to update a book
@app.put("/books/{book_id}")
def update_book(book_id: int):
    pass

# TODO: Implement DELETE /books/{book_id} endpoint to delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    pass

# Run with: uvicorn starter-code:app --reload
