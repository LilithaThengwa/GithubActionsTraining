from typing import List, Dict
from app.repository.book_repository import BookRepository

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def create_book(self, book: Dict) -> Dict:
        books = self.repository.get_all()
        
        if books:
            max_id = max(book["id"] for book in books)
        else:
            max_id = 0
        
        book["id"] = max_id + 1
        return self.repository.create(book)

    def get_book(self, book_id: int) -> Dict:
        return self.repository.get(book_id)

    def update_book(self, book_id: int, updated_book: Dict) -> Dict:
        return self.repository.update(book_id, updated_book)

    def delete_book(self, book_id: int) -> bool:
        return self.repository.delete(book_id)

    def get_all_books(self) -> List[Dict]:
        return self.repository.get_all()
    
# Provides a layer between the API (in routes) and the data repository (in book_repository.py). Handles business logic and comms with the repository.
# __init__ initialises the BookService by creating an instance of the BookRepository, this instance is used to preform data-related operations in te service methods.
# Each method calls the relevant method of the BookRepository.
# Self is a reference to the instance of the class, allows the method to access the attributes and methods of the current instance. 
# The arrow indicates a return type hint, makes cpde clearer and easier for devs to understand