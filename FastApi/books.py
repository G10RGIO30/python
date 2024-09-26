from fastapi import FastAPI
from models import Book

app = FastAPI()

#In-memory books list
books = [
    Book(id=1, title="Pride and Prejudice", author="Jane Austen", price=10.99),
    Book(id=2, title="Moby-Dick", author="Herman Melville", price=12.99),
    Book(id=3, title="Wuthering Heights", author="Emily Brontë", price=9.99),
    Book(id=4, title="Great Expectations", author="Charles Dickens", price=11.99),
    Book(id=5, title="To the Lighthouse", author="Virginia Woolf", price=13.99)
]

@app.get("/books")
def get_books():
    return books

@app.get("/books/{id}")
def get_book(id: int):
    for book in books:
        if book.id == id:
            return book

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return book

@app.put("/books/{id}")
def update_book(id: int, book: Book):
    for book in books:
        if book.id == id:
            book.title = book.title
            book.author = book.author
            book.price = book.price
            return book

@app.delete("/books/{id}")
def delete_book(id: int):
    for book in books:
        if book.id == id:
            books.remove(book)
            return book
