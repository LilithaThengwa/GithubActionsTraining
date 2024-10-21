import json
from typing import List, Optional

class BookRepository:
    def __init__(self, db_file=r'..\resources\book_list.json'):
        self.db_file = db_file

    def _read_data(self) -> List[dict]:
        with open(self.db_file, 'r') as file:
            return json.load(file)

    def _write_data(self, data: List[dict]) -> None:
        with open(self.db_file, 'w') as file:
            json.dump(data, file, indent=4)

    def create(self, book: dict) -> dict:
        books = self._read_data()
        books.append(book)
        self._write_data(books)
        return book

    def get(self, book_id: int) -> Optional[dict]:
        books = self._read_data()
        for book in books:
            if book['id'] == book_id:
                return book
        return None

    def update(self, book_id: int, updated_book: dict) -> Optional[dict]:
        books = self._read_data()
        for index, book in enumerate(books):
            if book['id'] == book_id:
                books[index] = updated_book
                self._write_data(books)
                return updated_book
        return None

    def delete(self, book_id: int) -> bool:
        books = self._read_data()
        for index, book in enumerate(books):
            if book['id'] == book_id:
                del books[index]
                self._write_data(books)
                return True
        return False

    def get_all(self) -> List[dict]:
        return self._read_data()

# Handles the data storage and retrieval mechanism for books.
#