from fastapi import APIRouter, HTTPException
from app.service.book_service import BookService
from app.model.book import Book

router = APIRouter()
service = BookService()

prefix_string = "/rest/api/books"

@router.post(f"{prefix_string}/add")
def create_book(book: Book):
    return service.create_book(book.dict())

@router.get(f"{prefix_string}/{{book_id}}")
def read_book(book_id: int):
    book = service.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put(f"{prefix_string}/{{book_id}}")
def update_book(book_id: int, updated_book: dict):
    book = service.update_book(book_id, updated_book)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete(f"{prefix_string}/{{book_id}}")
def delete_book(book_id: int):
    if not service.delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

@router.get(f"{prefix_string}")
def read_all_books():
    return service.get_all_books()

# router contains all teh endpoiont for interacting with books via API.
